#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import pygame
from pygame.locals import *
import time

class Display:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):

        self.CONF=CONF
        self.width=int(CONF["width"])
        self.height=int(CONF["height"])
        self.centerx=self.width/2
        self.centery=self.height/2
        
# Pygame modules initialization. Avoid general initialization because in some hardware you have no sound'
        pygame.font.init()
        pygame.display.init()
        
        if CONF["full_screen"] == "True":
            self.screen=pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((self.width,self.height))


# Change default mouse pointer
# "definition" is an array of strings containing a ascii map of an image made with "X" and "."
# Width and height must be multiply of 8
    def set_pointer(self, definition):
      size = (len(definition[0]), len(definition))
      print "Pointer size:", size
      data, mask = pygame.cursors.compile(definition, black='O',white='0',xor='o') 
      hotspot = (size[0]/2, size[1]/2)  # Set hotspot to centre
      pygame.mouse.set_cursor(size, hotspot, data, mask)



# Clear the screen
    def clean(self,color):
        self.screen.fill(color)
        pygame.display.flip()

# Fill the screen
    def fill(self,color):
        self.screen.fill(color)

# Show changes in the screen
    def show(self):
        pygame.display.flip()

# Print an image and returns current screen content
    def print_image(self, image, x, y):
        current_content=pygame.Surface((image.get_width(),image.get_height()))
        current_content.blit(self.screen,(0,0),(x,y,image.get_width(),image.get_height()))
        self.screen.blit(image, (x,y))
        return current_content

# Print a text string, centered as default
    def print_text(self, text, font, color=(0,0,0), x=-1, y=-1):
        rtext = font.render(text, 1, color)
        if x == -1:
            x=self.centerx - rtext.get_width() / 2
        if y == -1:
            y=self.centery - rtext.get_height() / 2
        self.screen.blit(rtext, (x,y))
        

    
 

