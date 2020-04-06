#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:09:38 2020
Handles assets and functions for game sounds.

@author: Matt
"""

import pygame.mixer

class Sounds:
    """Class for managing game sounds."""
    
    def __init__(self):
        """Initialize game sounds."""
        
        # Pre-initialize pygame.mixer
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        
        self.pop_sound = pygame.mixer.Sound("sounds/pop.ogg")
        self.throw_sound = pygame.mixer.Sound("sounds/throw.wav")
        self.throw_sound.set_volume(0.08)
        self.cough_sound = pygame.mixer.Sound("sounds/cough.wav")
        self.game_over_sound = pygame.mixer.Sound("sounds/gameover.wav")
        self.game_over_sound.set_volume(0.5)
    