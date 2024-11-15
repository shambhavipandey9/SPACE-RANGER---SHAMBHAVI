# egg blast
import pygame

class Egg(pygame.sprite.Sprite):
    def __init__(self,sr,pos_x, pos_y):
        super().__init__()
        # for egg
        self.screen = sr.screen
        self.image = pygame.image.load("image/egg.bmp")
        self.rect = self.image.get_rect()

        self.rect.centerx = pos_x + 30
        self.rect.centery = pos_y + 60
        self.speed_egg = 1
    def update(self):
        self.rect.y += self.speed_egg