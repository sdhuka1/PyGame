import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    # This is the overall class to manage game assets and behavior

    def __init__(self):
        # This is to initialize the game, and create game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        #This creates an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #This makes the Play button
        self.play_button = Button(self, "Play")

        #This sets the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #This starts the main loop for the game
        while True:
            self._check_events()

            if self.stats.game_activate:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
            
            self._update_screen()

            print(len(self.bullets))
            
    
    def _check_events(self):
        #This responds to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        #This starts a new game when the player clicks Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_activate:
            #This resets the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_activate = True
            #This hides the mouse cursor
            pygame.mouse.set_visible(False)

            #This gets rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #This creates a new fleet and centers the ship
            self._create_fleet()
            self.ship.center_ship()
    
    def _check_keydown_events(self, event):
        #This responds to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        #This responds to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #This creates a new bullet and adds it to the bullet group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #This updates the position of bullets and gets rid of old bullets
        #This updates bullet positions
        self.bullets.update()
        #This gets rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()        

    def _check_bullet_alien_collision(self):
        #This responds to bullet-alien collisions
        #This removes any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #This detroys existing bullets and creates a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    
    def _update_aliens(self):
        #This checks if the fleet is at an edge, then updates the position of all the aliens in the fleet
        self._check_fleet_edges()
        #This updates the positions of all the aliens in the fleet
        self.aliens.update()

        #This looks for an alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #This looks for aliens that have hit the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        #This responds to the ship being hit by an alien

        if self.stats.ships_left > 0:
            #This decrements ships_left
            self.stats.ships_left -= 1

            #This gets rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #This creates a new fleet and centers the ship
            self._create_fleet()
            self.ship.center_ship()

            #This pauses the game
            sleep(0.5)
        else:
            self.stats.game_activate = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        #This checks if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit
                self._ship_hit()
                break
    
    def _create_fleet(self):
        #This creates the fleet of aliens
        #This creates an alien and finds the number of aliens in a row
        #Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #This determines the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #This creates the full fleet of aliens
        for row_number in range(number_rows):
            #This creates the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        #This creates an alien and places it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        #This responds appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #This drops the entire fleet and changes the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #This updates the images on the screen and flips them to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #This draws the play button if the game is inactive
        if not self.stats.game_activate:
            self.play_button.draw_button()

        #This makes the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #This makes the game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()