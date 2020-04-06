#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:58:48 2020
Tracks game statistics.

@author: Matt
"""

import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
        # Settings for high score JSON file.
        self.filename = "high_score.json"
        
        # Load in the high score from file, othewise set to zero.
        self.load_high_score()       
            
    def load_high_score(self):
        """Read the high score from file, otherwise set to zero."""
        try:
            with open(self.filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
            
    def write_high_score(self):
        """Write the high score to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.high_score, f)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    

