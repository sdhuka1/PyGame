import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #This creates a class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #This initializes the alien and sets its starting position
        super().__init__()
        self.screen = ai_game.screen

        #This loads the alien image and sets its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #This starts each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #This stores the alien's exact horizontal position
        self.x = float(self.rect.x)
        