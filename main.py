import pygame
import random
import time
from CheeringObject import CheeringObject
from Coin import Coin
from Spawn import Spawn
from Button import Button
from Projectile import Projectile
from Corona_Proj import Corona_Proj
from Lose import Lose
import player
pygame.init()
# ////////////////////////////////////// game settings /////////////////////////////////////////////

run = True
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
lose = False
# ////////////////////////////////////////////////  background managing    ////////////////////////////////////
bg_list = [pygame.image.load('images/backgrounds/bg.jpg'), pygame.image.load('images/backgrounds/bg2.jpg'),
           pygame.image.load('images/backgrounds/bg3.png'), pygame.image.load('images/backgrounds/bg4.jpg')]
bg_index = 0
# ///////////////////////////////////////////////// variables assignments ////////////////////////////////////
cor_pro_shooting_right_now = False
cor_pro = None
t_spawn_created_list = []
jump_counter_random = random.randint(1, 5)
t_lvl_up = 0
play_lvl_up = 3
maors_girl = pygame.image.load('images/others/maors_girl.png')
coins_counter = 0
is_shooting = False
coin_image = pygame.image.load('images/others/coin.png')
sneeze_image = pygame.image.load('images/others/sneeze.png')
corona_image = pygame.image.load('images/bullets/corona.png')
bullets = []
spawn_list = []
direction = -1
t_0 = 0
t0_hit_image = 0
enemy_bullets = []
mp_amount = 100
play_game = False
coins = 0
# /////////////////////////////////////// music settings ////////////////////////////////////////////
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
lvl_up_sound = pygame.mixer.Sound('sounds/lvlup.wav')
lose_sound = pygame.mixer.Sound('sounds/lose_sound.wav')
gong = pygame.mixer.Sound('sounds/gong.wav')
pygame.display.set_caption("2D shooting game")
shot = pygame.mixer.Sound('sounds/shot.wav')
bruh = pygame.mixer.Sound('sounds/bruh.wav')
ploo = pygame.mixer.Sound('sounds/ploo.wav')
konichiwa = pygame.mixer.Sound('sounds/konichiwa.wav')
brk = pygame.mixer.Sound('sounds/brk.wav')
pygame.mixer_music.load('sounds/bg_music.wav')
enemy_shot = pygame.mixer.Sound('sounds/enemy_shot.wav')
hit_sound = pygame.mixer.Sound('sounds/hit_sound.wav')
coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')
laugh = pygame.mixer.Sound('sounds/laugh.wav')
sneeze_sound = pygame.mixer.Sound('sounds/sneeze.wav')
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
hp_text = font.render("HP", True, green, None)
score_counter = 0
displayed_score_counter = 0
display_counter = font.render(": " + str(displayed_score_counter) + "        :", True, black, None)
score = pygame.image.load('images/others/score.png')
# ////////////////////////////////////////////// fix and set hp mp//////////////////////////////////////////////////////

mp_printed_text = font2.render(str(100 - len(bullets)), True, black, None)


def redraw_game(dror_char, bullets, coin_image):
    coins_text = font.render(str(coins_counter), True, black, None)
    screen.blit(bg_list[bg_index % 4], (0, 0))
    screen.blit(coin_image, (440, 15))
    screen.blit(mp_text, (175, 20))
    screen.blit(hp_text, (20, 20))
    screen.blit(display_counter, (400, 25))
    pygame.draw.rect(screen, blue, (215, 20, 100 - 20 * len(bullets), 20), 0)
    # sneeze
    if coins_counter >= 3:
        screen.blit(sneeze_image, (501, 5))
    pygame.draw.rect(screen, green, (60, 20, dror_char.hp, 20), 0)
    hp_printed_text = font2.render(str(dror_char.adjust_hp()) + '/100', True, black, None)
    mp_printed_text = font2.render(str(100 - len(bullets) * 20) + '/100', True, black, None)
    screen.blit(mp_printed_text, (245 - len(bullets) * 5, 24))
    screen.blit(hp_printed_text, (max(60, dror_char.hp), 24))
    screen.blit(coins_text, (480, 25))
    screen.blit(score, (320, 7))
    dror_char.draw(screen, is_shooting)
    pygame.display.update()


dror_char = player.Player()
maor = Spawn(590, 300, 'images/faces/maor.png', 'images/faces/maor2.png', 5, konichiwa, 'images/bullets/asian.png',
             time.perf_counter(), random.randint(2, 7), t_spawn_created_list, displayed_score_counter)
ido = Spawn(590, 300, 'images/faces/ido.png', 'images/faces/ido2.png', 5, ploo, 'images/bullets/shnitzel.png',
            time.perf_counter(), random.randint(2, 7), t_spawn_created_list, displayed_score_counter)
tom = Spawn(590, 300, 'images/faces/tom.png', 'images/faces/tom2.png', 5, bruh, 'images/bullets/chains.png',
            time.perf_counter(), random.randint(2, 7), t_spawn_created_list, displayed_score_counter)
bar = Spawn(590, 300, 'images/faces/bar.png', 'images/faces/bar2.png', 5, brk, 'images/bullets/penisr.png',
            time.perf_counter(), random.randint(2, 7), t_spawn_created_list, displayed_score_counter)
t_spawn_created_list = []
ammo_list = ['asian.png', 'shnitzel.png', 'chains.png']
childs_list = [[maor, 'images/bullets/asian.png', konichiwa, 'images/faces/maor.png', 'images/faces/maor2.png'],
               [ido, 'images/bullets/shnitzel.png', ploo, 'images/faces/ido.png', 'images/faces/ido2.png'],
               [tom, 'images/bullets/chains.png', bruh, 'images/faces/tom.png', 'images/faces/tom2.png'],
               [bar, 'images/bullets/penisr.png', brk, 'images/faces/bar.png', 'images/faces/bar2.png']]
spawn_time_random = random.randint(2, 5)
play_button = Button(535, 0, 'images/others/play_button.png')
lose_button = Lose()
coins_list = []
coins_time_random = random.randint(3, 6)
maors_girl_object = CheeringObject(500, 400, maors_girl, laugh)

while run:
    # ////////////////////////////////////////// timings variables //////////////////////////////////////
    spawn_counter = time.perf_counter()
    jump_counter = time.perf_counter()
    coins_spawn_counter = time.perf_counter()
    enemy_time_counter = time.perf_counter()
    game_time = time.perf_counter()
    pygame.time.delay(100)
    # ///////////////////////////////////////////////////////////////////////////////////////////////////
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            run = False
    redraw_game(dror_char, bullets, coin_image)

    keys = pygame.key.get_pressed()
    dror_char.move(keys)
    # ///////////////////////////////////////// play button ///////////////////////////////////////////////////////
    play_button.draw(screen)
    if play_button.click(play_game, mouse_click, mouse_pos):
        coins_time_random += coins_spawn_counter
        dror_char.hp = 100
        if lose_button.lose:
            spawn_time_random += spawn_counter - lose_button.lose_interval_list[-1]
        else:
            spawn_time_random += spawn_counter
        play_game = True
        lose_button.play = False
        lose_button.lose = False
    # ////////////////////////////////////////// lose button //////////////////////////////////////////////////////
    if dror_char.hp == 0:
        score_counter = 0
        lose_button.draw(screen)
        if lose_button.play is False:
            lose_button.sound_play()
        lose_button.lose = True
        coins_list = []
        spawn_list = []
        bullets = []
        play_game = False
    # //////////////////////////////////////////// bg + lvl up ///////////////////////////////////////////////////////
    bg_index = displayed_score_counter // 3
    if 1 == displayed_score_counter / play_lvl_up and displayed_score_counter != 0 and play_game is True:
        lvl_up_sound.play()
        play_lvl_up += 3
        t_lvl_up = time.perf_counter()

    if displayed_score_counter % 3 == 0 and displayed_score_counter != 0 and \
            play_game is True and game_time - t_lvl_up < 1:
        screen.blit(pygame.image.load('images/others/lvl_up_text.png'), (200, 100))
    # //////////////////////////////////////////// coins   //////////////////////////////////////////////////

    if coins_spawn_counter > coins_time_random and play_game is True:
        coins_time_random += random.randint(3, 6)
        coins_list.append(Coin(random.randint(50, 600), random.randint(50, 450), coins_list))
    for coin in coins_list:
        coin.draw(screen)
        if coin.within_hitbox(dror_char) is True:
            coin.destroy()
            coins_counter += 1
    # /////////////////////////////////////// summoning childs //////////////////////////////////////////////////
    if play_game is True and lose_button.lose is False:
        if spawn_counter > spawn_time_random:
            spawn_time_random += random.randint(max(1, 2 - displayed_score_counter // 30),
                                                max(2, 5 - displayed_score_counter // 10))
            random_child_n = random.randint(0, 2)
            random_y = random.randint(50, 300)
            spawn_list.append(Spawn(590, random_y, childs_list[random_child_n][3],
                                    childs_list[random_child_n][4], 5,
                                    childs_list[random_child_n][2], childs_list[random_child_n][1],
                                    game_time, enemy_time_counter + random.randint(2, 8), t_spawn_created_list,
                                    displayed_score_counter))
    # /////////////////////////////////////// enemy bullets   ////////////////////////////////////////////////////
    for enemy_bullet in enemy_bullets:
        enemy_bullet.dror_in_range(dror_char, enemy_bullets)
        if enemy_bullet.x < - 40:
            enemy_bullets.pop(enemy_bullets.index(enemy_bullet))
        else:
            enemy_bullet.draw(screen)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for child in spawn_list:
        child.shoes_counter += 4
        if child.shoes_counter == 56:
            child.shoes_counter = 0
        child.jump_func()
        if jump_counter > jump_counter_random:
            child.jump = True
            jump_counter_random += random.randint(5, 5)
        if child.die_sound == konichiwa:
            maors_girl_object.draw(screen)
        if enemy_time_counter > child.shoot_interval:
            enemy_shot.play()
            enemy_bullets.append(Projectile(child.x - 30, child.y - 10, 'images/bullets/enemy_bullet.png', -1, bullets))
            child.shoot_interval += random.randint(2, 8)
        # print(child.shoot_interval)
        # child.collision()
        if child.x < 0:
            dror_char.hp = max(0, dror_char.hp - 10)
            spawn_list.pop(spawn_list.index(child))
        child.destroyed_animation(game_time)
        if child.alive is True:
            child.draw(screen, child.shoes_counter, child)
        else:
            spawn_list.pop(spawn_list.index(child))

    # ///////////////////////////////////////// time check /////////////////////////////////////////////////////////////

    if time.perf_counter() - t_0 > 0.5:
        dror_char.image = pygame.image.load('images/faces/drori_right.png')
        is_shooting = False
    if keys[pygame.K_LCTRL] and len(bullets) < 5:
        is_shooting = True
        shot.play()
        t_0 = time.perf_counter()
        if dror_char.right is True:
            dror_char.image = pygame.image.load('images/faces/drori_shoot_right.png')
        elif dror_char.left is True:
            dror_char.image = pygame.image.load('images/faces/drori_shoot_left.png')

        if dror_char.left is True:
            direction = -1
            bullet_image = 'images/bullets/defaultbulletl.png'

        else:
            direction = 1
            bullet_image = 'images/bullets/defaultbullet.png'

        for child in spawn_list:
            if dror_char.start_y + dror_char.height > child.hit_box[1] and \
                    dror_char.start_y < child.hit_box[1] + child.hit_box[2]:
                bullet_image = child.bullet

        bullets.append(Projectile(dror_char.start_x + (dror_char.width // 2), dror_char.start_y
                                  + (dror_char.height // 2), bullet_image, direction, bullets))

    for bullet in bullets:
        bullet.draw(screen)
        if bullet.within_hitbox(spawn_list, dror_char, t_spawn_created_list):
            bullets.pop(bullets.index(bullet))
            score_counter += 1
            displayed_score_counter += 1
            display_counter = font.render(str(displayed_score_counter), True, black, None)
        elif bullet.x > 640 or bullet.x < 0:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_a] and cor_pro_shooting_right_now is False and coins_counter >= 3:
        coins_counter -= 3
        sneeze_sound.play()
        cor_pro = Corona_Proj(dror_char.start_x + 10, dror_char.start_y + dror_char.height // 2, dror_char.right,
                              time.perf_counter())
        cor_pro_shooting_right_now = True

    if cor_pro_shooting_right_now is True:
        if game_time - cor_pro.time_created > 0.5:
            cor_pro_shooting_right_now = False
            cor_pro = None
            explosion_sound.play()
            n = len(spawn_list)
            for child in spawn_list:
                child.destroy(t_spawn_created_list)
            dror_char.hp += n * 10
            score_counter += n
        else:
            cor_pro.draw(screen)

    pygame.display.update()
pygame.quit()
