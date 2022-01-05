"""
Author: Mona
Date: January 5th, 2021
Name: instructions
Description: The instructions screen of poisonous pyramids
"""

#Import modules
import pygame, sys, os, time
from pygame.locals import * 


# If you get the no available video device error, copy and paste the below code ##
import platform, os


#Create window
pygame.init() 
size = (850,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Poisonous Pyramids') 
screen = pygame.display.get_surface() 


running=True


while running:
    #Display instructions
    surface = pygame.image.load("images/instructions.png")
    screen.blit(surface,(0,0))

        
    #Allow user to exit the game
    for event in events:       
        if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
            screen.fill(THECOLORS["white"])
            screen.blit(myfont_body.render("Goodbye", 1, (0,0,0)), (0,0))
            pygame.display.update()            
            time.sleep(1)
            running = False 
