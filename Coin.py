import pygame


def coins_listener(coins_list, screen, dror_char):
    for coin in coins_list:
        coin.draw(screen)
        if coin.within_hitbox(dror_char) is True:
            coin.destroy()
            return 1
    return 0


class Coin:
    def __init__(self, x, y, lst):
        self.coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/others/coin.png')
        self.hit_box = (self.x, self.y, 30, 30)
        self.lst = lst

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hit_box, 1)

    def within_hitbox(self, dror_char):
        if self.hit_box[0] - dror_char.width <= dror_char.start_x <= self.hit_box[0] + 30 and \
                self.hit_box[1] - dror_char.height - 20 <= dror_char.start_y <= self.hit_box[1] + 30:
            return True

    def destroy(self):
        self.lst.pop(self.lst.index(self))
        self.coin_sound.play()
