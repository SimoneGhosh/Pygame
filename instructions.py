"""
Author: Mona
Date: January 5th, 2021
Name: instructions
Description: The instructions screen of poisonous pyramids
"""

#Import modules
import pygame, sys, os, time
from pygame.locals import *
from pygame.color import THECOLORS


# If you get the no available video device error, copy and paste the below code ##
import platform, os


#Create window
pygame.init() 
size = (850,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Poisonous Pyramids') 
screen = pygame.display.get_surface() 

#font
myfont_medium= pygame.font.SysFont("times new roman", 23)
myfont_title = pygame.font.SysFont("Papyrus", 60)

running=True

while running:
    #Display instructions
    surface = pygame.image.load("images/instructions.png")
    screen.blit(surface,(0,0))
    title=myfont_title.render("INSTRUCTIONS", True, THECOLORS["antiquewhite"])
    screen.blit(title, (120,50))
    
    x=65
    y=160
    with open("textFiles/instructions.txt") as word_file:
        for sentence in word_file:
            screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            y+=40
    pygame.display.flip()

    events=pygame.event.get()
    #Allow user to exit the game
    for event in events:       
        if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
            
            running = False 
