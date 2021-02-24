import pygame


class Button(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.add_time = True
        self.play_counter = 0
        self.time_list = []
        self.gong = gong = pygame.mixer.Sound('sounds/gong.wav')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def click(self, play_game, mouse_click, mouse_pos):
        if mouse_click[0] == 1 and 620 >= mouse_pos[0] >= 556 and 15 <= mouse_pos[1] <= 50 and play_game is False:
            self.gong.play()
            return True
        return False

