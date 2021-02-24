import pygame


class Corona_Proj():
    def __init__(self, x, y, direction, time_created):
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
