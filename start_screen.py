#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:29:34 2020
Module for creating start screen.

@author: Matt
"""

import pygame.font

HALF_WIDTH = 75

class PlayButton:
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.center
        self.rect.y += HALF_WIDTH
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
class Title:
    """Attirbutes and methods for creating the game title on start screen."""
    
    def __init__(self, ai_game, msg):
        """Initialize the title box attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set dimensions and properties.
        self.width, self.height = 450, 200
        self.color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60, bold = 0, italic = 1)
        
        # Build the box's rect.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.center
        self.rect.y -= HALF_WIDTH
        
        # Prep the box.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn message into a rendered image and center text on it."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw(self):
        # Draw blankrectangle and then draw message.
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
class DifficultyMessage:
    """
    Attributes and methods for creating 
    difficulty setting message on start screen.
    """
    
    def __init__(self, ai_game):
        """Initialize the difficulty message attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties.
        self.width, self.height = 800, 100
        self.color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60, bold = 0, italic = 1)
        
        # Build the boxs' rect.
        self.rect1 = pygame.Rect(0,0, self.width, self.height)
        self.rect1.center = self.screen_rect.center
        self.rect1.y += HALF_WIDTH / 2 - 10
        self.rect2 = pygame.Rect(0,0, self.width, self.height)
        self.rect2.center = self.screen_rect.center
        self.rect2.y += HALF_WIDTH + 10
        
        # Prep the boxes.
        self.msg1 = "Press number to select difficulty"
        self.msg2 = "1: Easy, 2: Normal, 3: Hard, 4: Sick"
        
        self._prep_msg()
        self._prep_msg()
        
        # Set difficulty message to on by default
        self.msg_on = True
        
    def _prep_msg(self):
        """Turn message into a rendered image and center text on it."""
        self.msg1_image = self.font.render(self.msg1, True, self.text_color, 
                                          self.color)
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.center = self.rect1.center
        
        self.msg2_image = self.font.render(self.msg2, True, self.text_color, 
                                          self.color)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect2.center
        
    def draw(self):
        # Draw blankrectangle and then draw message.
        self.screen.fill(self.color, self.rect1)
        self.screen.fill(self.color, self.rect2)
        self.screen.blit(self.msg1_image, self.msg1_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
    
        