"""
Program Name: alien.py

Author: Shrrayash Srinivasan

Purpose: Got the alien class set up. Each alien is a sprite that can move to the right, check screen boundaries, 
and be drawn on the screen.

Date: November 18, 2025
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from alien_navy import AlienFleet

class Alien(Sprite):
     def __init__(self, fleet: 'AlienFleet', y: float, x: float, side='right'):
          super().__init__()
          self.fleet = fleet
          self.screen = fleet.game.screen
          self.boundaries = fleet.game.screen.get_rect()
          self.settings = fleet.game.settings
          self.side = side

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
        vertical_speed = self.settings.fleet_speed         
        self.y += vertical_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x
     
     def check_edges(self):
         """Done to ensure no alien ship is breaching the bottom/top edges of the screen."""
         return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top) 


     def draw_alien(self):
          self.screen.blit(self.image, self.rect)