import pygame


class Projectile(object):

    def __init__(self, x, y, image, direction, bullets):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 30
        self.image = pygame.image.load(image)
        self.hit_box = (self.x + 5, self.y + 13, 40, 27)
        self.mp = 5 - len(bullets)
        self.hit_sound = pygame.mixer.Sound('sounds/hit_sound.wav')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.hit_box = (self.x + 5, self.y + 13, 40, 27)
        #pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        self.x += self.vel * self.direction

    def within_hitbox(self, spawn_list, dror_char, t_spawn_created_list):
        for child in spawn_list:
            if self.hit_box[0] + child.hit_box[2] > child.hit_box[0] and\
                    self.hit_box[1] + self.hit_box[3] > child.hit_box[1] and\
                    self.hit_box[1] < child.hit_box[1]\
                    + child.hit_box[2] and \
                    self.hit_box[0] < child.hit_box[0] + child.hit_box[2]:
                child.destroy(t_spawn_created_list)
                dror_char.hp = min(dror_char.hp + 10, 100)
                return True
        return False

    def child_in_range(self, spawn_list):
        for child in spawn_list:
            if self.hit_box[1] + self.hit_box[3] > child.hit_box[1] and \
                    self.hit_box[1] < child.hit_box[1] + child.hit_box[2]:
                return child.bullet
        return False

    def dror_in_range(self, dror_char, enemy_bullets):
        for enemy_bullet in enemy_bullets:
            if self.hit_box[1] + self.hit_box[3] > dror_char.hit_box[1] and \
                    self.hit_box[1] < dror_char.hit_box[1] + dror_char.hit_box[2] and \
                    self.hit_box[0] < dror_char.hit_box[0] + dror_char.hit_box[2]:
                enemy_bullets.pop(enemy_bullets.index(enemy_bullet))
                self.hit_sound.play()
                dror_char.hp = max(dror_char.hp - 10, 0)
