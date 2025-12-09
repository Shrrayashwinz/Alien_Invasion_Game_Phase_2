"""
Program Name: hud.py

Author: Shrrayash Srinivasan

Purpose:
    Defines the HUD (Heads-Up Display) class for the Alien Invasion game.
    The HUD is responsible for rendering scores, levels, and remaining lives
    on the screen during gameplay.

Date: November 28, 2025
"""

import pygame.font


class HUD:
    """Heads-Up Display for the Alien Invasion game."""

    def __init__(self, game):
        """Initialize HUD resources."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.game_stats = game.game_stats

        # Font and padding setup
        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.HUD_font_size
        )
        self.padding = 20

        self._setup_life_image()
        self.update_scores()
        self.update_level()

    def update_scores(self):
        """Update all score-related HUD elements."""
        self._update_max_score()
        self._update_score()
        self._update_hi_score()
        self.update_level()

    def _setup_life_image(self):
        """Prepare the image used to represent remaining lives."""
        self.life_image = pygame.image.load(self.settings.hero_ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image,
            (self.settings.hero_ship_w, self.settings.hero_ship_h)
        )
        self.life_rect = self.life_image.get_rect()

    def _update_score(self):
        """Render the current score and position it on the screen."""
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(
            score_str, True, self.settings.text_color, None
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """Render the maximum score and position it at the top-right corner."""
        max_score_str = f"MAX Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(
            max_score_str, True, self.settings.text_color, None
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """Render the high score and position it at the top-center."""
        hi_score_str = f"HI Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(
            hi_score_str, True, self.settings.text_color, None
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def update_level(self):
        """Render the current level and position it on the screen."""
        level_str = f"LEVEL: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(
            level_str, True, self.settings.text_color, None
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.padding + self.life_rect.height + self.padding

    def _draw_lives(self):
        """Draw the remaining lives (hero ships) on the screen."""
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.hero_ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draw all HUD elements onto the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self._draw_lives()
        self.screen.blit(self.level_image, self.level_rect)






    









    






















    









    


