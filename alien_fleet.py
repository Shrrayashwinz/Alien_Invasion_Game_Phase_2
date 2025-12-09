"""
Program Name: alien_fleet.py

Author: Shrrayash Srinivasan and Kaden Breinholt <3 (pals)

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
          self.fleet_speed = self.settings.fleet_speed

          self.create_fleet()


     def create_fleet(self):
          """Create a fleet of aliens arranged in a grid formation."""

          alien_w = self.settings.alien_w
          alien_h = self.settings.alien_h
          screen_w = self.settings.screen_w
          screen_h = self.settings.screen_h

          # FIX: returns now in correct order (fleet_w, fleet_h)
          fleet_w, fleet_h = self.calculate_fleet_size(
               alien_w, screen_w, alien_h, screen_h
          )

          # FIX: centers fleet in left half + vertically
          x_offset, y_offset = self.calculate_offsets(
               alien_w, alien_h, screen_w, fleet_w, fleet_h
          )

          self._create_rectangle_fleet(
               alien_w, alien_h, fleet_h, fleet_w, x_offset, y_offset
          )


     def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         for row in range(fleet_h):
             for col in range(fleet_w):
                 current_x = alien_w * col + x_offset
                 current_y = alien_h * row + y_offset
                 if col % 2 == 0 or row % 2 == 0:
                    continue

                 # FIX: correct x, y order
                 self._create_alien(current_x, current_y)


     def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
          """Calculate horizontal and vertical offsets to center the fleet on screen."""

          # left-half width
          left_half = screen_w // 2

          # total fleet pixel size
          final_fleet_w = fleet_w * alien_w
          final_fleet_h = fleet_h * alien_h

          # padding around the fleet
          pad = 20

          # center fleet inside the LEFT HALF
          x_offset = (left_half - final_fleet_w) // 2

          # vertical centering inside entire screen
          y_offset = (self.settings.screen_h - final_fleet_h) // 2

          # apply padding
          x_offset = max(pad, x_offset)
          y_offset = max(pad, y_offset)

          return x_offset, y_offset


     def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
          """Calculates the fleet size so that it fits the screen"""

          # padding (left/top/bottom)
          padding = int(alien_w * 0.5)

          # usable horizontal space = left half minus horizontal padding on both sides
          left_half_w = screen_w // 2
          usable_w = max(0, left_half_w - (padding * 2))

          # usable vertical space = full screen height minus vertical padding
          usable_h = max(0, screen_h - (padding * 2))

          # spacing = 2 * alien_w)
          visible_cols = max(1, usable_w // (alien_w * 2))

          # spacing = 2 * alien_h
          visible_rows = max(1, usable_h // (alien_h * 2))

          # convert visible counts to grid cell dimensions
          grid_w = visible_cols * 2
          grid_h = visible_rows * 2

          # debug print
          print(f"{grid_h}, {grid_w}")

          return grid_w, grid_h


     def _create_alien(self, current_x: int, current_y: int):

          # FIX: corrected x, y order
          new_alien = Alien(self, current_x, current_y, side='right')
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
          """What to do when the alien fleet collides with a bullet or the hero ship."""
          return pygame.sprite.groupcollide(self.fleet, other_group, True, True)


     def check_fleet_right(self):
          alien: Alien
          for alien in self.fleet:
               if alien.rect.right >= self.settings.screen_w:
                    return True
          return False


     def check_destroyed_status(self):
          """Returns whether the fleet is entirely destroyed."""
          return not self.fleet

          
     