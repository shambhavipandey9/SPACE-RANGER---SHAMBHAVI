# laser
import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,sr):
        super().__init__()
        self.image = pygame.image.load("image/laser.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        # so that the laser comes out from the rockets top
        self.rect.center = sr.rocket.rocket_rect.midtop
        # for laser speed
        self.laser_speed = 2

    def update(self):
        self.rect.y -= self.laser_speed 