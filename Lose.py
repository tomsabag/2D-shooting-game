import pygame
import time


class Lose:

    def __init__(self, x=180, y=200):
        self.x = x
        self.y = y
        self.image = 'images/others/loser.png'
        self.lose_sound = pygame.mixer.Sound('sounds/lose_sound.wav')
        self.lose = False
        self.play = False
        self.lose_interval_list = []

    def draw(self, screen):
        screen.blit(pygame.image.load('images/others/loser.png'), (self.x, self.y))

    def sound_play(self):
        self.lose_sound.play()
        self.lose_interval_list.append(time.perf_counter())
        self.play = True
