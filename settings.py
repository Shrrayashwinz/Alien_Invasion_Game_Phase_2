"""
Program Name: Lab12_pcarswel_Shrrayash_1.py
Author: Shrrayash Srinivasan
Purpose: Defined settings for the Alien Invasion game, including screen dimensions, asset paths, ship and bullet behavior, 
and initial ship placements. 
Date: November 16, 2025
"""

from pathlib import Path

class Settings:
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.hero_ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.hero_ship_w = 40
        self.hero_ship_h = 60
        self.hero_ship_speed = 4

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 10
        self.bullet_w = 20
        self.bullet_h = 75
        self.bullet_amount = 15

        self.ship_side = "left"  

        
        self.alien_file = Path.cwd() / 'Assets' /  'images'   / 'enemy_4.png'
        self.fleet_speed = 1
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
        self.fleet_drop_speed = 25
        self.alien_side = "right"

