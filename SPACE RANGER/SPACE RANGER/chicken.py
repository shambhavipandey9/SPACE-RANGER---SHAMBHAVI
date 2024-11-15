#chicken 
import pygame

class Chicken(pygame.sprite.Sprite):
    def __init__(self,sr):
        super().__init__()

        self.screen = sr.screen
        # for chicken
        self.image = pygame.image.load("image/hen.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = 60
        self.rect.y = 58