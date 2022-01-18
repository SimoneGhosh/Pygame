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
from pygame import mixer

#If you get the no available video device error
import platform, os

#This code is necessary for python to work on tdsb computers
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Initial library itself
pygame.init() 



#Set-up the main screen display window
size = (850,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Poisonous Pyramid') 
screen = pygame.display.get_surface() 

#Change the logo of our window
pygame_icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(pygame_icon)

#Clock
clock = pygame.time.Clock()
refresh_rate=30


#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
myfont_special=pygame.font.SysFont("Papyrus", 40)
myfont_medium = pygame.font.SysFont("times new roman", 22)
lesson_font_big = pygame.font.SysFont("Papyrus", 75)
test=pygame.display.get_driver()


# The Game Loop
running=True
show="ending 1"
try:
    while running:
        clock.tick(60)
        #to scroll through the endings, press the space bar!!
        
        if show == "instructions":
            surface = pygame.image.load("images/instructions.png")
            screen.blit(surface,(0,0))
                    
            title=myfont_title.render("INSTRUCTIONS", True, THECOLORS["antiquewhite"])
            screen.blit(title, (120,50))
                    
            
            x=75
            y=160
            with open("textFiles/instructions.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40
        
            pygame.draw.rect(screen, THECOLORS['brown'], (350, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (385, 550))
        events=pygame.event.get()
  
        
        for event in events:
            if event.type==KEYDOWN:
                if show=="ending 1" and event.key==K_SPACE:
                        show= "ending 2"
                        
                elif show=="ending 2" and event.key==K_SPACE:
                        show= "ending 3a"
                        
                elif show=="ending 3a" and event.key==K_SPACE:
                        show= "ending 3b"
                        
                elif show=="ending 3b" and event.key==K_SPACE:
                        show= "ending 4"
            #Exit    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                x=0
                y=0
                running=False
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly

