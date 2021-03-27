import pygame
class CheeringObject:
    def __init__(self, x, y, image, sound):
        self.x = x
        self.y = y
        self.image = image
        self.sound = sound
        self.sound_played = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.sound_played is False:
            self.sound_played = True
            self.sound.play()


