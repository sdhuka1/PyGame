import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    # This is the overall class to manage game assets and behavior

    def __init__(self):
        # This is to initialize the game, and create game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #This sets the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #This starts the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    
    def _check_events(self):
        #This responds to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #This moves the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        #This updates the images on the screen and flips them to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #This makes the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #This makes the game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()