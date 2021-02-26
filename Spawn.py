import pygame
import time

score_counter = 0
displayed_score_counter = 0
class Spawn(object):
    def __init__(self, x, y, image, image2, vel, die_sound, bullet, t_created, shoot_interval, t_spawn_created_list, displayed_score_counter):
        self.shoes_list = [pygame.image.load(f"shoes/{i}.gif") for i in range(60)]
        self.shoes_counter = 0
        self.image = pygame.image.load(image)
        self.image2 = pygame.image.load(image2)
        self.die_sound = die_sound
        self.vel = vel + displayed_score_counter // 3
        self.x = x
        self.y = y
        self.life = 100
        self.hit_box = (self.x, self.y, 60, 60)
        self.alive = True
        self.kill_time = 999
        self.bullet = bullet
        self.t_created = t_created
        self.shoot_interval = shoot_interval
        self.jump_count = 10
        self.jump = False

        t_spawn_created_list.append(t_created)

    def draw(self, screen, shoes_counter, child):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.shoes_list[shoes_counter], (child.x - 20, child.y + 40))
        # green = pygame.draw.rect(screen, (0, 255, 0), (50, 50, 40, 15), 0)
        self.hit_box = (self.x, self.y, 60, 60)
        #pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        if self.alive is True:
            self.x -= self.vel

    def destroy(self, t_spawn_created_list):
        t_spawn_created_list.pop(t_spawn_created_list.index(self.t_created))
        self.die_sound.play()
        self.kill_time = time.perf_counter()
        self.image = self.image2

        #score_counter += 1
        #displayed_score_counter += 1
        pygame.font.SysFont(None, 30)

    def destroyed_animation(self, game_time):
        if (game_time - self.kill_time) > 0.05:
            self.alive = False

    def jump_func(self):
        if self.jump is True:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= self.jump_count ** 2 * 0.5 * neg
                self.jump_count -= 1
        else:
            self.jump = False
            self.jump_count = 10
