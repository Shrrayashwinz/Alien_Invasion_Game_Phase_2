"""
Program Name: hero_ship.py

Author: Shrrayash Srinivasan

Purpose: Handles the hero ship initialization, movement, drawing, and firing processors for the Alien Invasion game.
Integrates with the Arsenal class and ensures the ship faces the center of the screen at the right side.

Date: November 21, 2025
"""

import pygame
from typing import TYPE_CHECKING
from arsenal import Arsenal 

if TYPE_CHECKING:
    from lab12_ssrinivasan3 import AlienInvasion

class Ship:
    """Manages the hero ship's stats, initialization, movement, bullets, and collision detection."""
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal', side='left'):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.side = side
        self.arsenal = arsenal

        self.image = pygame.image.load(self.settings.hero_ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.hero_ship_w, self.settings.hero_ship_h)
        )

        if side == "left":
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = self.image.get_rect()
            self.rect.left = 0
        elif side == "right":
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
            self.rect.right = self.boundaries.right

        self.rect.centery = self.boundaries.centery

        self.moving_up = False
        self.moving_down = False

        self.y = float(self.rect.y)

    def update(self):
        """Update ship position and arsenal state."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Adjust ship's vertical position based on movement flags and speed."""
        temp_speed = self.settings.hero_ship_speed

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self):
        """Draw the ship and its bullets on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet(self.rect.center, self.side)
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False


    def _center_ship(self):
        """Re-center ship vertically after collision."""

        self.rect.centery = self.boundaries.centery
        self.y = float(self.rect.y)
        if self.side == "left":
            self.rect.left = 0
        elif self.side == "right":
            self.rect.right = self.boundaries.right

