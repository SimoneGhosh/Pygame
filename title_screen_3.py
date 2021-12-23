"""
Author: Simone and Mona
Date: 2021-12-23
Name: title_screen_3
Description: Title screen of poisonous pyramids
"""

#Import modules
import pygame, sys, os, time
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform, os

pygame.init() 
size = (850,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Poisonous Pyramids') 
screen = pygame.display.get_surface() 


# The screen is the Drawing window
surface = pygame.image.load("bluebg.jpg")
screen.blit(surface,(0,0))

# Setting up the font and the size 
myfont = pygame.font.SysFont("Papyrus", 60)
test=pygame.display.get_driver()

#Here is whre you can put items that don't move
text=myfont.render("POISONOUS", True, THECOLORS["brown"])
text2=myfont.render("PYRAMIDS", True, THECOLORS["brown"])
screen.blit(text, (175,50))
screen.blit(text2, (225,150))

pygame.display.flip() # flip all changes onto the display window

# The Game Loop
running=True
try:
    while running:
        # The Event Loop #
        events=pygame.event.get()
        for event in events: 
            if event.type == QUIT:
                running=False   # Stop the program, it's detected quit...
        
  
finally:
    pygame.quit()  # Keep this IDLE friendly     
        
# Event Handling End #