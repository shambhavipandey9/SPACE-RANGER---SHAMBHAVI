# space ranger
import sys
import pygame

from rocket import Rocket
from laser import Laser
from chicken import Chicken
from egg import Egg
from time import sleep

class SpaceRanger:
    def __init__(self):
        pygame.init() 
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800,600))
        self.rocket = Rocket(self)
        self.laser = pygame.sprite.Group()
        self.chicken = pygame.sprite.Group()
        self.egg = pygame.sprite.Group()
        self._chicken()
        self.attack = True
        self.rocket_life = 5
        self.game_not_over = False
        self.text_font = pygame.font.Font(None , 35 )
        self.game_score = 0
        self.high_score = 0
        # for sound
        self.laser_sound = pygame.mixer.Sound("sound1/laser.wav")
        self.chicken_sound = pygame.mixer.Sound("sound1/chicken.wav")
        self.rocket_hit = pygame.mixer.Sound("sound1/rocket_hit.wav")
        # title
        self.title_image = pygame.image.load("image/title.png").convert_alpha()
        self.title_rect =  self.title_image.get_rect(topleft = (0,0))
        pygame.display.set_caption("SPACE RANGER")

    def run_game(self):
        # to run the game
        while True:
            if self.game_not_over:
                self._check_event()
                self.laser.update()
                self._laser_update()
                self._time()
                self.egg.update()
                self._egg_update()
                
            else:
                self.game_score = 0
                self.rocket_life = 5
                self.attack =True
                self.rocket.position_update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                            self.game_not_over = True
            
            self._update_screen()

    def _check_event(self):
        # to check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_d:
                    self.rocket.move_right = True
                elif event.key == pygame.K_a:
                    self.rocket.move_left = True
                elif event.key == pygame.K_SPACE:
                    self._laser_fire()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.rocket.move_right = False
                elif event.key == pygame.K_a:
                    self.rocket.move_left = False

    def _laser_fire(self):  # to fire laser
        new_laser = Laser(self)
        self.laser.add(new_laser)
        self.laser_sound.play()

    def _laser_update(self): # another function for the lasers
        for laser in self.laser.copy():
            if laser.rect.bottom <= 0 :
                self.laser.remove(laser)
    
        self._collision_of_laser_chicken() # didnt work from space

    def _collision_of_laser_chicken(self):
        collision = pygame.sprite.groupcollide(self.chicken , self.laser , True , True)
        if collision:
            self.game_score += 50  
            self.chicken_sound.play()

        if not self.chicken:
            self.egg.empty()
            self.laser.empty()
            self._chicken()
            self.attack = True
            sleep(0.5)
            
    def _chicken(self):
        row , no_of_chicken = 3 , 6
        for row_num in range(row):
            for no_chicken in range(no_of_chicken):
                chicken = Chicken(self)
                chicken_width , chicken_height = chicken.rect.size
                chicken.rect.x = chicken_width + 2*(chicken_width)*(no_chicken)
                chicken.rect.y = chicken_height + 2*(chicken_height)*(row_num)
                self.chicken.add(chicken)

    def _time(self):
        
        self.current_time = (pygame.time.get_ticks()//1000) 
        if self.current_time % 3 == 0:
            self._egg()
            
    def _egg(self):

        for chicken in self.chicken.sprites():
    
            if chicken.rect.x - 15 <= self.rocket.rocket_rect.x and self.rocket.rocket_rect.x <= chicken.rect.x +15 and self.attack: 
                pos_x = chicken.rect.x
                pos_y = chicken.rect.y
                egg = Egg(self,pos_x ,pos_y )
                self.egg.add(egg)
                self.attack = False
                break

    def _egg_update(self):
            for egg in self.egg.copy():
                if egg.rect.bottom >= 600:
                    self.egg.remove(egg)
                    self.attack = True
            self._collision_of_egg_rocket()

    def _collision_of_egg_rocket(self):
        for egg in self.egg.sprites():
            if egg.rect.colliderect(self.rocket.rocket_rect):
                self._rocket_hit()
                break
        
    def _rocket_hit(self):
        if self.rocket_life > 0:
            self.rocket_life -= 1
            # sound 
            self.rocket_hit.play()
            # restart all the stuff
            self.egg.empty()
            self.laser.empty()
            self.attack = True
            # sleep the game
            sleep(0.5)

        if self.rocket_life == 0:
            self.chicken.empty()
            self._chicken()
            self.game_not_over = False

    def _dash_board(self):
        # for score
        self.score = self.text_font.render("SCORE  "f"{self.game_score}",True,(60,60,60))
        self.score_rect = self.score.get_rect(center = (400,20))
        self.screen.blit(self.score , self.score_rect)
        # for life
        self.life = self.text_font.render("LIFE  "f"{self.rocket_life}",True , (60,60,60))
        self.life_rect = self.life.get_rect(center = (700,20))
        self.screen.blit(self.life , self.life_rect)
        # for high score
        self.high = self.text_font.render("HIGH SCORE  "f"{self.high_score}", True , (60,60,60))
        self.high_rect = self.high.get_rect(center = (120,20))
        self.screen.blit(self.high , self.high_rect)
        self._high_score()
        
    def _high_score(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score

    def _update_screen(self):
        self.screen.fill("white")
        self.rocket.blit_rocket()
        self._dash_board()
        self.laser.draw(self.screen)
        self.laser.update()
        self.chicken.draw(self.screen) 
        self.egg.draw(self.screen)
        self.rocket.boundaries()
        self.rocket.update()

        if self.game_not_over == False:
            self.screen.blit(self.title_image , self.title_rect)

        pygame.display.update()

if __name__ == "__main__":
    sr = SpaceRanger()
    sr.run_game() 