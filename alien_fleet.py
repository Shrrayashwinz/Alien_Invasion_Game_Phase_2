"""
Program Name: alien_navy.py

Author: Shrrayash Srinivasan

Purpose: Defines the AlienFleet class, which manages the creation, movement, collision detection, and rendering of a fleet of aliens 
in the Alien Invasion game.

Date: November 21, 2025
"""
import pygame
from typing import TYPE_CHECKING
from alien import Alien


if TYPE_CHECKING:
     from lab12_ssrinivasan3 import AlienInvasion

class AlienFleet:
     """Manages the fleet of the aliens in the alien invasion game."""
     def __init__(self, game: 'AlienInvasion'):
          self.game = game
          self.settings = game.settings
          self.fleet = pygame.sprite.Group()
          self.fleet_direction = self.settings.fleet_direction
          #self.fleet_drop_speed = self.settings.fleet_drop_speed
          self.fleet_speed = self.settings.fleet_speed

          self.create_fleet()
    

     def create_fleet(self):
          """Create a fleet of aliens arranged in a grid formation."""
          alien_w = self.settings.alien_w
          alien_h = self.settings.alien_h
          screen_w = self.settings.screen_w
          screen_h = self.settings.screen_h

          fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

          x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

          self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         for row in range(fleet_h):
             for col in range(fleet_w):
                 current_x = alien_w * col + x_offset
                 current_y = alien_h * row + y_offset
                 if col % 2 == 0 or row % 2 == 0:
                    continue
                 self._create_alien(current_x, current_y)

     def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
         """Calculate horizontal and vertical offsets to center the fleet on screen."""
         half_screen = self.settings.screen_h//2
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         x_offset = int((screen_w - fleet_horizontal_space)//2)
         y_offset = int((half_screen-fleet_vertical_space)//2)
         return x_offset,y_offset

     def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
         """Calculates the fleet size so that it fits the screen"""        
         fleet_w = (screen_w//alien_w) - 1
         fleet_h = ((screen_h/2)//alien_h) + 1

         if fleet_w % 2 == 0:
              fleet_w -=1
            
         else:
              fleet_w -= 2

         if fleet_h % 2 == 0:
              fleet_h -= 1
         else:
              fleet_h -= 2

         
         return int(fleet_w), int(fleet_h)
     
     def _create_alien(self, current_y: int, current_x: int):
          new_alien = Alien(self, current_y, current_x, side='right')

          self.fleet.add(new_alien)


     def _check_fleet_edges(self):
          alien: Alien
          for alien in self.fleet:
               if alien.check_edges():
                    self._shift_fleet_right()
                    self.fleet_direction *= -1
                    break
     
     def _shift_fleet_right(self):
          for alien in self.fleet:
              alien.x += self.fleet_speed

     def update_fleet(self):
          self._check_fleet_edges()
          self.fleet.update()

     def draw(self):
          alien: 'Alien'
          for alien in self.fleet:
               alien.draw_alien()
     
     def check_collisions(self, other_group):
          """WHat to do when the alien fleet collides with a bullet or the hero ship."""
          return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
     

     def check_fleet_right(self):
          alien: Alien
          for alien in self.fleet:
               if alien.rect.right >= self.settings.screen_w:
                    return True
               return False
     
     def check_destroyed_status(self):
          """Returns should the fleet be entirely destroyed."""
          return not self.fleet
