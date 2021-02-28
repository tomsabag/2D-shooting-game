import pygame


class Corona_Proj():
    def __init__(self, x, y, direction, time_created):
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
        self.shooting = False
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/bullets/corona.png')
        self.vel = 25
        self.direction = direction
        self.time_created = time_created

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.direction == 1:
            self.x += self.vel
        else:
            self.x -= self.vel

    def shoot(self, game_time, screen, spawn_list, t_spawn_created_list, dror_char):
        if game_time - self.time_created > 0.5:
            self.shooting = False
            self.explosion_sound.play()
            n = len(spawn_list)
            for child in spawn_list:
                child.destroy(t_spawn_created_list)
            dror_char.hp += n * 10
            return n
        else:
            self.draw(screen)
            return 0
