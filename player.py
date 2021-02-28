import time
import pygame

from Projectile import Projectile


class Player(object):
    def __init__(self, start_x=50, start_y=215, width=50, height=50):
        self.is_shooting = False
        self.hp = 100
        self.hp_printed_text = pygame.font.SysFont(None, 17).render(str(self.adjust_hp()) + '/100', True, (0, 0, 0), None)
        self.is_hit = 0
        self.skateboard_list = [pygame.image.load(f"skateboard/{max(0, 3*i - 1)}.gif") for i in range(30)]
        self.skateboard_counter = 15
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.vel = 15
        self.jump = False
        self.jump_count = 10
        self.left = False
        self.right = True
        self.image = pygame.image.load('images/faces/drori_right.png')
        self.hit_box = (self.start_x - 2, self.start_y, self.width + 5, self.height + 13)

    def draw(self, screen):
        if not self.is_shooting:
            if self.left is True:
                self.image = pygame.image.load('images/faces/drori_left.png')
            elif self.right is True:
                self.image = pygame.image.load('images/faces/drori_right.png')
        screen.blit(self.image, (self.start_x, self.start_y))
        screen.blit(self.skateboard_list[self.skateboard_counter], (self.start_x - 15, self.start_y + 30))
        self.skateboard_counter += 1
        if self.skateboard_counter == 30:
            self.skateboard_counter = 15

        self.hit_box = (self.start_x - 2, self.start_y, self.width + 5, self.height + 13)
        #pygame.draw.rect(screen, red, self.hitbox, 1)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.start_x > 0:
            self.left = True
            self.right = False
            self.start_x -= self.vel

        if keys[pygame.K_RIGHT] and self.start_x < 640 - self.width:
            self.right = True
            self.left = False
            self.start_x += self.vel

        if not self.jump:
            if keys[pygame.K_UP] and self.start_y > 10:
                self.start_y -= self.vel
            if keys[pygame.K_DOWN] and self.start_y < 480 - self.height - 35:
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

    def adjust_hp(self):
        return max(0, min(self.hp, 100))

    def shoot(self, spawn_list, bullets, shot):
        self.is_shooting = True
        shot.play()
        if self.right is True:
            self.image = pygame.image.load('images/faces/drori_shoot_right.png')
        elif self.left is True:
            self.image = pygame.image.load('images/faces/drori_shoot_left.png')

        if self.left is True:
            direction = -1
            bullet_image = 'images/bullets/defaultbulletl.png'

        else:
            direction = 1
            bullet_image = 'images/bullets/defaultbullet.png'

        for child in spawn_list:
            if self.start_y + self.height > child.hit_box[1] and \
                    self.start_y < child.hit_box[1] + child.hit_box[2]:
                bullet_image = child.bullet

        bullets.append(Projectile(self.start_x + (self.width // 2), self.start_y
                                  + (self.height // 2), bullet_image, direction, bullets))

