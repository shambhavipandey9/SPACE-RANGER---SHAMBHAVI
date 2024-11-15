# rocket
import pygame

class Rocket():
    def __init__(self,sr):
        self.screen = sr.screen
        # for player i.e. rocket
        self.rocket_image = pygame.image.load("image/rocket.bmp")
        self.rocket_rect = self.rocket_image.get_rect(midbottom = (400,600))

        self.move_right = False
        self.move_left = False
    
    def update(self):
        
        if self.move_right: # for ship move right
            self.rocket_rect.x += 1

        elif self.move_left: # for ship move left 
            self.rocket_rect.x -= 1

    def boundaries(self):
        if self.rocket_rect.x >= 740 :
            self.move_right = False
        if self.rocket_rect.x <= 0  :
            self.move_left = False

    def position_update(self):
        self.rocket_rect.midbottom = (400, 600)

    def blit_rocket(self):
        self.screen.blit(self.rocket_image , self.rocket_rect)