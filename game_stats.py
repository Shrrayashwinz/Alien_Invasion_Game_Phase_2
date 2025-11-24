"""
Program Name: game_stats.py
Author: Shrrayash Srinivasan
Purpose: Tracks the stats and lives of our hero ship.
. 
Date: November 22, 2025
"""

class GameStats():

    """Tracks stats for the hero ship (so far)"""

    def __init__(self, hero_ships_limit):
        self.hero_ships_left = hero_ships_limit