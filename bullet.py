import pygame
from pygame.sprite import sprite

class Bullet(Sprite):
    #This creates a class to manage bullets fired from the ship

    def __init__(self, ai_game):
        #This creates a bullet object at the ship's current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.bullet_color

        #This creates a bullet rect at (0,0) and then sets the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #This stores the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        #This moves the bullet up the screen
        #This updates the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #This updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #This draws the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)