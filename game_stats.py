"""
Program Name: game_stats.py

Author: Shrrayash Srinivasan

Purpose:
    Tracks and manages game statistics for the Alien Invasion game.
    This includes hero ship lives, score, high score, maximum score,
    and level progression. Stats are saved and loaded from a JSON file.

Date: November 22, 2025
"""

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab12_ssrinivasan3 import AlienInvasion


class GameStats:
    """
    Tracks and manages statistics for the Alien Invasion game.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize statistics and load saved scores.


        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats(game)

    def init_saved_scores(self):
        """
        Initialize high score from saved file if available.
        Creates a new file if none exists.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """
        Save the current high score to a JSON file.
        """
        scores = {'hi_score': self.hi_score}
        contents = json.dumps(scores, indent=4)

        try:
            self.path.write_text(contents)
        except FileNotFoundError as fnfe:
            print("File not found!:", fnfe)

    def reset_stats(self, game: 'AlienInvasion'):
       """Reset statistics for a new game session."""
       self.hero_ships_left = game.settings.starting_hero_ship_count
       self.score = 0
       self.level = 1

    def update_level(self):
       """Increment the game level when the player clears a wave."""
       self.level += 1

    def update(self, collisions: dict):
        """
        Update statistics based on collisions.


        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """
        Update the maximum score for the current session.
        """
        if self.score > self.max_score:
            self.max_score = self.score
        print("MAX:", self.max_score)

    def _update_hi_score(self):
        """
        Update the high score if the current score exceeds it.
        Saves the new high score to file.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()
        print("HI:", self.hi_score)

    def _update_score(self, collisions: dict):
        """
        Update the score based on alien collisions.

        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        print("SCORE:", self.score)

    def update_level(self):
        """
        Increment the game level when the player clears a wave.
        """
        self.level += 1
        print("LEVEL:", self.level)
