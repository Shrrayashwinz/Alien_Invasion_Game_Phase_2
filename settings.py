"""
Program Name: settings.py

Author: Shrrayash Srinivasan

Purpose:
    Defines the Settings class for the Alien Invasion game.
    This includes screen dimensions, asset paths, ship and bullet behavior,
    alien fleet properties, button styling, and difficulty scaling.

Date: November 16, 2025
"""

from pathlib import Path


class Settings:
    """
    A class to store all settings for the Alien Invasion game.
    """

    def __init__(self):
        """Initialize static game settings."""
        # General game settings
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Background
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Difficulty scaling
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Hero ship settings
        self.hero_ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.hero_ship_w = 40
        self.hero_ship_h = 60

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'greenlaser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        # Ship placement
        self.ship_side = "right"

        # Alien fleet settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        # Button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (47, 130, 158)

        # Text and font settings
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 24
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

        # Initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.

        Includes ship speed, bullet speed, bullet count, alien fleet speed,
        and alien point values.
        """
        self.hero_ship_speed = 5
        self.starting_hero_ship_count = 4

        self.bullet_speed = 7
        self.bullet_amount = 10
        self.bullet_w = 25
        self.bullet_h = 80

        self.fleet_speed = 0.5
        self.fleet_drop_speed = 2
        self.fleet_drop_speed = 25   
        self.alien_points = 50

    def increase_difficulty(self):
        """
        Increase game difficulty by scaling speed values.

        Called when the player advances to a new level.
        """
        self.fleet_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.hero_ship_speed *= self.difficulty_scale



