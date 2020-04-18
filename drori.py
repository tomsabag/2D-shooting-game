import pygame
import random
import time
pygame.init()
# //////////////////////////////////////FUTURE TO DO LIST //////////////////////////////////////////
#let childs shoot bullets too at drori, at random pace, reducing hp as well,
#make levels - different music, childs harder to kill, change background image and music
#make missions = in a certain time - kill a certain amount
# ////////////////////////////////////// game settings /////////////////////////////////////////////
run = True
screen = pygame.display.set_mode((640, 480))
background_image = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
# /////////////////////////////////////// music settings ////////////////////////////////////////////
pygame.display.set_caption("drr mbdd")
shot = pygame.mixer.Sound('shot.wav')
chains = pygame.mixer.Sound('chains.wav')
burp = pygame.mixer.Sound('burp.wav')
laugh = pygame.mixer.Sound('laugh.wav')
bite = pygame.mixer.Sound('bite.wav')
pygame.mixer_music.load('bg_music.wav')
enemy_shot = pygame.mixer.Sound('enemy_shot.wav')
hit_sound = pygame.mixer.Sound('hit_sound.wav')
pygame.mixer_music.play(-1)
# /////////////////////////////////////////////// color settings /////////////////////////////////////////
blue = (30, 144, 255)
green = (50, 205, 50)
black = (0, 0, 0)
red = (255, 0, 0)

# /////////////////////////////////////////////// game settings //////////////////////////////////////////
font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 17)
mp_text = font.render("MP", True, blue, None)
hp_amount = 100
hp_text = font.render("HP", True, green, None)
score_counter = 0
displayed_score_counter = 0
escaped_counter = 0
display_counter = font.render(": " + str(displayed_score_counter), True, black, None)
score = pygame.image.load('score.png')
# ///////////////////////////////////////////////// shoes ////////////////////////////////////////////////////
shoes_list = [pygame.image.load('shoes/0.gif'), pygame.image.load('shoes/1.gif'), pygame.image.load('shoes/2.gif'),
              pygame.image.load('shoes/3.gif'), pygame.image.load('shoes/4.gif'), pygame.image.load('shoes/5.gif'),
              pygame.image.load('shoes/6.gif'), pygame.image.load('shoes/7.gif'), pygame.image.load('shoes/8.gif'),
              pygame.image.load('shoes/9.gif'), pygame.image.load('shoes/10.gif'), pygame.image.load('shoes/11.gif'),
              pygame.image.load('shoes/12.gif'), pygame.image.load('shoes/13.gif'), pygame.image.load('shoes/14.gif'),
              pygame.image.load('shoes/15.gif'), pygame.image.load('shoes/16.gif'), pygame.image.load('shoes/17.gif'),
              pygame.image.load('shoes/18.gif'), pygame.image.load('shoes/19.gif'), pygame.image.load('shoes/20.gif'),
              pygame.image.load('shoes/21.gif'), pygame.image.load('shoes/22.gif'), pygame.image.load('shoes/23.gif'),
              pygame.image.load('shoes/24.gif'), pygame.image.load('shoes/25.gif'), pygame.image.load('shoes/26.gif'),
              pygame.image.load('shoes/27.gif'), pygame.image.load('shoes/28.gif'), pygame.image.load('shoes/29.gif'),
              pygame.image.load('shoes/30.gif'), pygame.image.load('shoes/31.gif'), pygame.image.load('shoes/32.gif'),
              pygame.image.load('shoes/33.gif'), pygame.image.load('shoes/34.gif'), pygame.image.load('shoes/35.gif'),
              pygame.image.load('shoes/36.gif'), pygame.image.load('shoes/37.gif'), pygame.image.load('shoes/38.gif'),
              pygame.image.load('shoes/39.gif'), pygame.image.load('shoes/40.gif'), pygame.image.load('shoes/41.gif'),
              pygame.image.load('shoes/42.gif'), pygame.image.load('shoes/43.gif'), pygame.image.load('shoes/44.gif'),
              pygame.image.load('shoes/45.gif'), pygame.image.load('shoes/46.gif'), pygame.image.load('shoes/47.gif'),
              pygame.image.load('shoes/48.gif'), pygame.image.load('shoes/49.gif'), pygame.image.load('shoes/50.gif'),
              pygame.image.load('shoes/51.gif'), pygame.image.load('shoes/52.gif'), pygame.image.load('shoes/53.gif'),
              pygame.image.load('shoes/54.gif'), pygame.image.load('shoes/55.gif'), pygame.image.load('shoes/56.gif'),
              pygame.image.load('shoes/57.gif'), pygame.image.load('shoes/58.gif'), pygame.image.load('shoes/59.gif')]
shoes_counter = 0
# ///////////////////////////////////////////////// variables assignments ////////////////////////////////////
bullets = []
spawn_list = []
direction = -1
t_0 = 0
t0_hit_image = 0
enemy_bullets = []
drori_is_hit_counter = 0
mp_amount = 100


# ////////////////////////////////////////////// fix and set hp mp//////////////////////////////////////////////////////
def adjust_hp(hp_amount):
    global escaped_counter
    global drori_is_hit_counter
    global score_counter
    if escaped_counter == 1:
        hp_amount -= 10
    if drori_is_hit_counter == 1:
        hp_amount -= 10
    if score_counter == 1:
        hp_amount += 10
    escaped_counter = 0
    drori_is_hit_counter = 0
    score_counter = 0
    print(score_counter)
    return max(0, min(hp_amount, 100))


hp_printed_text = font2.render(str(adjust_hp(hp_amount)) + '/100', True, black, None)
mp_printed_text = font2.render(str(100 - len(bullets)), True, black, None)
# ////////////////////////////////////////////////////// Drori class ///////////////////////////////////////////////////
class Drori(object):
    def __init__(self, start_x=50, start_y=215, width=50, height=50):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.vel = 15
        self.jump = False
        self.jump_count = 10
        self.left = False
        self.right = True
        self.image = pygame.image.load('drori.png')
        self.hitbox = (self.start_x - 2, self.start_y, self.width + 5, self.height + 13)

    def draw(self):
        screen.blit(self.image, (self.start_x, self.start_y))
        self.hitbox = (self.start_x - 2, self.start_y, self.width + 5, self.height + 13)
        #pygame.draw.rect(screen, red, self.hitbox, 1)

    def move(self):
        right = False
        left = False
        if keys[pygame.K_LEFT] and self.start_x > 0:
            self.left = True
            self.right = False
            self.start_x -= self.vel
            self.image = pygame.image.load('drori.png')

        if keys[pygame.K_RIGHT] and self.start_x < 640 - self.width:
            self.right = True
            self.left = False
            self.start_x += self.vel
            self.image = pygame.image.load('drori.png')

        if not self.jump:
            if keys[pygame.K_UP] and self.start_y > 0:
                self.start_y -= self.vel
            if keys[pygame.K_DOWN] and self.start_y < 480 - self.width:
                self.start_y += self.vel
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.start_y -= self.jump_count ** 2 * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10


class Spawn(object):

    def __init__(self, x, y, image, image2, vel, die_sound, bullet, t_created, shoot_interval):
        self.image = pygame.image.load(image)
        self.image2 = pygame.image.load(image2)
        self.die_sound = die_sound
        self.vel = vel
        self.x = x
        self.y = y
        self.life = 100
        self.hit_box = (self.x, self.y, 60, 60)
        self.alive = True
        self.kill_time = 999
        self.bullet = bullet
        self.t_created = t_created
        self.shoot_interval = shoot_interval

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(shoes_list[shoes_counter], (child.x - 20, child.y + 40))
        # green = pygame.draw.rect(screen, (0, 255, 0), (50, 50, 40, 15), 0)
        self.hit_box = (self.x, self.y, 60, 60)
        #pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        if self.alive is True:
            self.x -= self.vel

    def destroy(self):
        self.die_sound.play()
        self.kill_time = time.perf_counter()
        self.image = self.image2
        global displayed_score_counter
        global score_counter
        score_counter += 1
        displayed_score_counter += 1

        global display_counter
        display_counter = font.render(str(displayed_score_counter), True, black, None)

    def destroyed_animation(self):
        if (game_time - self.kill_time) > 0.05:
            self.alive = False

    def shoot(self):
        pass

    def spawn(self):
        pass


    '''def collision(self):
        for bullet in bullets:
            if bullet.within_hitbox() is True:
                print('yes')
                bullets.pop(bullets.index(bullet))
                self.destroy()'''


class Projectile(object):

    def __init__(self, x, y, image, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 30
        self.image = pygame.image.load(image)
        self.hit_box = (self.x + 5, self.y + 13, 40, 27)
        self.mp = 5 - len(bullets)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.hit_box = (self.x + 5, self.y + 13, 40, 27)
        #pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        if self.direction == 1:
            self.x += self.vel
        else:
            self.x -= self.vel

    def within_hitbox(self):
        for child in spawn_list:
            if self.hit_box[0] + child.hit_box[2] > child.hit_box[0] and\
                    self.hit_box[1] + self.hit_box[3] > child.hit_box[1] and\
                    self.hit_box[1] < child.hit_box[1]\
                    + child.hit_box[2] and \
                    self.hit_box[0] < child.hit_box[0] + child.hit_box[2]:
                child.destroy()
                return True
        return False

    def child_in_range(self):
        for child in spawn_list:
            if self.hit_box[1] + self.hit_box[3] > child.hit_box[1] and\
                    self.hit_box[1] < child.hit_box[1] + child.hit_box[2]:
                return child.bullet
        return False

    def dror_in_range(self):
        for enemy_bullet in enemy_bullets:
            if self.hit_box[1] + self.hit_box[3] > dror_char.hitbox[1] and \
                    self.hit_box[1] < dror_char.hitbox[1] + dror_char.hitbox[2] and \
                    self.hit_box[0] < dror_char.hitbox[0] + dror_char.hitbox[2]:
                enemy_bullets.pop(enemy_bullets.index(enemy_bullet))
                global drori_is_hit_counter
                hit_sound.play()
                drori_is_hit_counter += 1
    '''def decide_bullet(self):
        if bullet.child_in_range() is False:
            return 'defaultbullet.png'
        else:
            return self.bullet'''


def redraw_game():
    global hp_amount
    global hp_printed_text
    global mp_printed_text
    global shoes_counter
    screen.blit(background_image, (0, 0))
    shoes_counter += 4
    if shoes_counter == 56:
        shoes_counter = 0
    screen.blit(mp_text, (175, 20))
    screen.blit(hp_text, (20, 20))
    screen.blit(display_counter, (420, 25))
    pygame.draw.rect(screen, blue, (215, 20, 100 - 20 * len(bullets), 20), 0)
    hp_amount = adjust_hp(hp_amount)
    #hp_amount = min(100, max(0, 100 - 10 * escaped_counter -
    #               10 * drori_is_hit_counter + score_counter * 10))
    pygame.draw.rect(screen, green, (60, 20, hp_amount, 20), 0)
    hp_printed_text = font2.render(str(adjust_hp(hp_amount)) + '/100', True, black, None)
    mp_printed_text = font2.render(str(100 - len(bullets) * 20) + '/100', True, black, None)
    screen.blit(mp_printed_text, (245 - len(bullets) * 5, 24))
    screen.blit(hp_printed_text, (max(60, hp_amount), 24))
    screen.blit(score, (340, 7))
    pygame.display.update()


dror_char = Drori()
maor = Spawn(590, 300, 'maor.png', 'maor2.png', 5, laugh, 'asian.png', time.perf_counter(), random.randint(2, 7))
ido = Spawn(590, 300, 'ido.png', 'ido2.png', 5, burp, 'shnitzel.png', time.perf_counter(), random.randint(2, 7))
tom = Spawn(590, 300, 'tom.png', 'tom2.png', 5, chains, 'chains.png', time.perf_counter(), random.randint(2, 7))
bar = Spawn(590, 300, 'bar.png', 'bar2.png', 5, bite, 'penisr.png', time.perf_counter(), random.randint(2, 7)) ############### fix bar2 and bullet

ammo_list = ['asian.png', 'shnitzel.png', 'chains.png']
childs_list = [[maor, 'asian.png', laugh, 'maor.png', 'maor2.png'], [ido, 'shnitzel.png', burp, 'ido.png', 'ido2.png'],
               [tom, 'chains.png', chains, 'tom.png', 'tom2.png'], [bar, 'penisr.png', bite, 'bar.png', 'bar2.png']]
spawn_time_random = random.randint(2, 5)

while run:
    spawn_counter = time.perf_counter()
    enemy_time_counter = time.perf_counter()
    game_time = time.perf_counter()
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redraw_game()
    keys = pygame.key.get_pressed()
    dror_char.move()
    dror_char.draw()
    #childs_list[r][0].draw()

    #   /////////////////////////////////////// summoning childs //////////////////////////////////////////////////
    if spawn_counter > spawn_time_random:
        spawn_time_random += random.randint(2, 5)
        random_child_n = random.randint(0, 3)
        random_y = random.randint(50, 300)
        spawn_list.append(Spawn(590, random_y, childs_list[random_child_n][3],
                                childs_list[random_child_n][4], 5,
                                childs_list[random_child_n][2], childs_list[random_child_n][1],
                                game_time, enemy_time_counter + random.randint(2, 8)))
    # /////////////////////////////////////// enemy bullets ///////////////////////////////////////////////////////
    for enemy_bullet in enemy_bullets:
        enemy_bullet.dror_in_range()
        if enemy_bullet.x < 0:
            enemy_bullets.pop(enemy_bullets.index(enemy_bullet))
        else:
            enemy_bullet.draw()
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for child in spawn_list:
        if enemy_time_counter > child.shoot_interval:
            enemy_shot.play()
            enemy_bullets.append(Projectile(child.x - 30, child.y - 10, 'enemy_bullet.png', -1))
            child.shoot_interval += random.randint(2, 8)
        #print(child.shoot_interval)
        #child.collision()
        if child.x < 0:
            spawn_list.pop(spawn_list.index(child))
            escaped_counter += 1
        child.destroyed_animation()
        if child.alive is True:
            child.draw()
        else:
            spawn_list.pop(spawn_list.index(child))

    #  //////////////////////////////////////// projectiles check /////////////////////////////////////////////////


    # ///////////////////////////////////////// time check /////////////////////////////////////////////////////////////

    if time.perf_counter() - t_0 > 0.5:
        dror_char.image = pygame.image.load('drori.png')

    if keys[pygame.K_LCTRL] and len(bullets) < 5:
        shot.play()
        t_0 = time.perf_counter()
        dror_char.image = pygame.image.load('drori2.png')

        if dror_char.left is True:
            direction = -1
        else:
            direction = 1

        bullet_image = 'defaultbullet.png'
        for child in spawn_list:
            if dror_char.start_y + dror_char.height > child.hit_box[1] and\
                    dror_char.start_y < child.hit_box[1] + child.hit_box[2]:
                bullet_image = child.bullet

        bullets.append(Projectile(dror_char.start_x + (dror_char.width // 2), dror_char.start_y
                                  + (dror_char.height // 2), bullet_image, direction))

    for bullet in bullets:
        bullet.draw()
        if bullet.within_hitbox() is True or bullet.x > 640:
            bullets.pop(bullets.index(bullet))
        #if bullet.x < 640 and len(spawn_list) > 0 and bullet.x <= spawn_list[0].x:
         #   bullet.draw()


    pygame.display.update()
pygame.quit()

