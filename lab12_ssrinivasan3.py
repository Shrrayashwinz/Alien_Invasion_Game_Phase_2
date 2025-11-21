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
from alien_ship import Ship
from arsenal import Arsenal 
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

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

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(1.7)

        self.alien_ship = Ship(self, Arsenal(self), side='right')
        self.alien = Alien(self, 10,10)


    def run_game(self):
        while self.running:
            self._check_events()
            self.alien_ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.alien_ship.draw()
        self.alien.draw_alien()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event): 
        if event.key == pygame.K_KP_8:
            self.alien_ship.moving_up = False
        elif event.key == pygame.K_KP_2:
            self.alien_ship.moving_down = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_KP_8:
            self.alien_ship.moving_up = True
        elif event.key == pygame.K_KP_2:
            self.alien_ship.moving_down = True
        elif event.key == pygame.K_KP_0:
            if self.alien_ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
