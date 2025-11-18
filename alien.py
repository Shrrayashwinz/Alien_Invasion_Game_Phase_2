"""
Program Name: alien.py

Author: Shrrayash Srinivasan

Purpose: Got the alien class set up.

!!!!THIS IS A TUTORIAL CODE!!!!


Date: November 18, 2025
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from lab12_ssrinivasan3 import AlienInvasion

class Alien(Sprite):
     def __init__(self, game: 'AlienInvasion', y: float, x: float):
          super().__init__()
          self.screen = game.screen
          self.boundaries = game.screen.get_rect()
          self.settings = game.settings

          self.image = pygame.image.load(self.settings.alien_file)
          self.image = pygame.transform.scale(
                self.image,
                (self.settings.alien_w, self.settings.alien_h)
          )
          
          self.rect = self.image.get_rect()
          self.rect.y = y          
          self.rect.x = x

          self.y = float(self.rect.y)          
          self.x = float(self.rect.x)

     def update(self):
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
             self.settings.fleet_direction *= -1
             self.x += self.settings.fleet_drop_speed
             
        self.y += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y
     
     def check_edges(self):
         return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top) 

     def draw_alien(self):
          self.screen.blit(self.image, self.rect)