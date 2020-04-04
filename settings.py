#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:47:03 2020
Gameplay settings for alien_invasion.py

@author: Matt
"""


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        #self.bullet_width = 3
        #self.bullet_height = 15
        self.bullet_color = (250,0,0)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 15

        # Level settings
        self.level = 1
        self.speedup_scale = 1.3
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self, level = 1):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.75 * level
        self.bullet_speed = 4 * level
        self.alien_speed = 1.5 * level
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
