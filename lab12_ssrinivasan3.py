"""
Program Name: Lab12_ssrinivasan3_#1.py

Author: Shrrayash Srinivasan

Purpose: This serves as the main module for the game Alien Invasion. It has all the necessary functions from the other files to 
ensure the game is operational! 

Date: November 21, 2025 
"""

import sys
import pygame
from settings import Settings
from hero_ship import Ship
from game_stats import GameStats
from arsenal import Arsenal 
from alien_fleet import AlienFleet
from time import sleep
from button import Button


class AlienInvasion:
    """This is the main control that managez the Alien Invasion game.
    
    """
    def __init__(self):
        """Initializes game resources, settings, and the needed objects."""
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_hero_ship_count)


        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        self.running = True
        self.clock = pygame.time.Clock()

        """The noises for the game."""

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.75)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact)
        self.impact_sound.set_volume(0.7)


        self.hero_ship = Ship(self, Arsenal(self), side='right')
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, "Play")
        self.game_active = False


    def run_game(self):
        """Starts the main game loop"""

        while self.running:
            self._check_events()
            if self.game_active:
               self.hero_ship.update()
               self.alien_fleet.update_fleet()
               self._check_collisions()
               self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Checks for collisions between the hero ship,the alien navy from the Alien Nation and the bullets
        fired by the hero ship."""

        if self.hero_ship.check_collisions(self.alien_fleet.fleet):
           self._check_game_status() 

        if self.alien_fleet.check_fleet_right():
            self._check_game_status()


        collisions = self.alien_fleet.check_collisions(self.hero_ship.arsenal.arsenal)
        if collisions:
           self.impact_sound.play()
           self.impact_sound.fadeout(1000)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            sleep(0.5)
       

    def _check_game_status(self):
        """What happens should the hero ship lose a life. Game ends when no lives are left."""


        if self.game_stats.hero_ships_left > 0: 
            self.game_stats.hero_ships_left -= 1
            self._reset_level()

            print("Lives left:", self.game_stats.hero_ships_left) 


    
        else:
          self.game_active = False
    

    def _reset_level(self):
        """Reset level by recreating alien fleet."""
        self.hero_ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
    
    def restart_game(self):
        #self.settings.initialize_dynamic_settings()
        self._reset_level()
        self.hero_ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Remake background and the other objects."""
        self.screen.blit(self.bg, (0, 0))
        self.hero_ship.draw()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
            
        pygame.display.flip()
      

    def _check_events(self):
        """Involves the keys involved with operating the ship and what to do to quit the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
               self._check_button_clicked()
    
    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
          self.restart_game()

    def _check_keyup_events(self, event): 
        if event.key == pygame.K_t:
            self.hero_ship.moving_up = False
            
        elif event.key == pygame.K_g:
            self.hero_ship.moving_down = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_t:
            self.hero_ship.moving_up = True

        elif event.key == pygame.K_g:
            self.hero_ship.moving_down = True
            
        elif event.key == pygame.K_SPACE:
            if self.hero_ship.fire():
                self.laser_sound.play()
                
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        






