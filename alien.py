"""
Program Name: alien.py

Author: Shrrayash Srinivasan

Purpose:
    Defines the Alien class. Each alien is a sprite that can move horizontally,
    check screen boundaries, and be drawn on the screen.

Date: November 18, 2025
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Manages the alien position, settings, and behavior in the Alien Invasion game."""

    def __init__(self, fleet: 'AlienFleet', y: float, x: float, side='right'):
        """
        Initialize an alien sprite.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        self.side = side

        # Load and scale alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        # Position alien
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store precise position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update alien's position based on fleet direction and speed."""
        # Move horizontally
        self.x += self.settings.fleet_speed * self.fleet.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        Return True if alien has reached screen edge.
        Used by fleet to decide when to drop down and reverse direction.
        """
        return (self.rect.right >= self.boundaries.right or
                self.rect.left <= 0)

    def draw_alien(self):
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)
