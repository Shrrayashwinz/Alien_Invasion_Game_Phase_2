"""
Program Name: bullet.py

Author: Shrrayash Srinivasan

Purpose: Defined the Bullet class with the use of the Sprite system. It is an important part of the alien ship firing mechanism and
the bullets fire out of the ship and the code is done specifically to track the movement and speed of the lasers.

Date: November 16, 2025
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab12_ssrinivasan3 import AlienInvasion

class Bullet(Sprite):
    """Bullet class to manage bullets fired by the player's ship."""
    def __init__(self, game: 'AlienInvasion', position, direction):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        if direction == 1:
            self.image = pygame.transform.rotate(self.image, -90)
        else:
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect(center=position)
        if direction == 1:
            self.rect.left = position[0]
        else:
            self.rect.right = position[0]

        self.x = float(self.rect.x)

        self.direction = direction
        self.speed = self.settings.bullet_speed

    def update(self):
        """Directly update the bullet's position based on its speed and direction."""
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)







