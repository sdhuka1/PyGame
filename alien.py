import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #This creates a class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #This initializes the alien and sets its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #This loads the alien image and sets its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #This starts each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #This stores the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        #This returns True if alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        #This moves the alien to the left or right
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x