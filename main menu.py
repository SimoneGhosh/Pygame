"""
Author: Simone
Date: 2021-12-23
Name: title_screen_3
Description: Title screen of poisonous pyramids
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

#Display background image
surface = pygame.image.load("pyramids.jpg")
screen.blit(surface,(0,0))

#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
test=pygame.display.get_driver()

#Titles 
title=myfont_title.render("POISONOUS", True, THECOLORS["brown"])
title_end=myfont_title.render("PYRAMIDS", True, THECOLORS["brown"])
sub_title=myfont_body.render("main menu", True, THECOLORS["brown"])

screen.blit(title, (175,50))
screen.blit(title_end, (225,125))
screen.blit(sub_title, (350,200))

pygame.display.flip() #flip all changes onto the display window

# The Game Loop
running=True
try:
    while running:
        # The Event Loop #
        events=pygame.event.get()
        
        #Button for instructions
        pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
        screen.blit(myfont_body.render("Instructions", 1, THECOLORS['antiquewhite']), (180,305))
        
        #Button for lesson
        pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
        screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (530,305))
        
        #Button for review
        pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
        screen.blit(myfont_body.render("Review", 1, THECOLORS['antiquewhite']), (205,410)) 
        
        #Button for quiz
        pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
        screen.blit(myfont_body.render("Quiz", 1, THECOLORS['antiquewhite']), (545,410))
        
        #Allow user to exit the game
        for event in events:       
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                screen.fill(THECOLORS["white"])
                screen.blit(myfont_body.render("Goodbye", 1, (0,0,0)), (0,0))
                pygame.display.update()            
                time.sleep(1)
                running = False        
        
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly     