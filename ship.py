import pygame

class Ship:
    #This creates a class to manage the ship

    def __init__(self, ai_game):
        #This initializes the ship and sets its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #This loads the ship image and gets its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #This starts each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #This stores a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        #This serves as a movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #This updates the ship's position based on the movement flag
        #This updates the ship's x value and not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #This updates the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #This draws the ship at its current location
        self.screen.blit(self.image, self.rect)