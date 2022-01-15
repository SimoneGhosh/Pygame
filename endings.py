"""
Author: Mona
Date: Jan 15, 2022
Name: quiz
Description: Poisonous pyramids interactive review endings
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

#This code is necessary for python to work on tdsb computers
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Clock
clock = pygame.time.Clock()
refresh_rate=30

#fonts
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
test=pygame.display.get_driver()


        
# The Game Loop
running=True
show="ending 1"
try:
    while running:
        
        clock.tick(60)
        
        if show == "ending 1":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake bite", 1, THECOLORS['antiquewhite']), (180,155))

            #death description
            x=5
            y=-15
            with open("textFiles/ending 1.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
        elif show =="ending 2":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake bite", 1, THECOLORS['antiquewhite']), (180,155))

            #death description
            x=5
            y=-15
            with open("textFiles/ending 2.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

        elif show =="ending 3a":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake attack", 1, THECOLORS['antiquewhite']), (180,155))

            #death description
            x=5
            y=-15
            with open("textFiles/ending 3a.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

        elif show =="ending 3b":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake attack", 1, THECOLORS['antiquewhite']), (180,155))

            #death description
            x=5
            y=-15
            with open("textFiles/ending 3b.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

        elif show =="ending 4":
            surface = pygame.image.load("images/treasure.png")
            screen.blit(surface,(0,0))
            #Success!
            screen.blit(myfont_title.render("You made it!", 1, THECOLORS['antiquewhite']), (180,155))

            #some praise
            screen.blit(myfont_body.render("You have successfully completed your missions!", 1, THECOLORS['antiquewhite']), (180,155))
            screen.blit(myfont_body.render("Now you live a comfortable and wealthy life!", 1, THECOLORS['antiquewhite']), (180,155))


                        
            
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly
