import pygame

class Ship:
    #This creates a class to manage the ship

    def __init__(self, ai_game):
        #This initializes the ship and sets its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #This loads the ship image and gets its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #This starts each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #This serves as a movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #This updates the ship's position based on the movement flag
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        #This draws the ship at its current location
        self.screen.blit(self.image, self.rect)