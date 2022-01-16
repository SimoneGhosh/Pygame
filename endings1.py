"""
Author: Mona
Date: Jan 15, 2022
Name: Interactive review endings
Description: Death and mission success endings.
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
myfont_medium= pygame.font.SysFont("times new roman", 23)#######add this font to main!
myfont_small = pygame.font.SysFont("times new roman", 15)
test=pygame.display.get_driver()

def main_menu_button():
    pygame.draw.rect(screen, THECOLORS['brown'], (330, 500, 170, 50))
    screen.blit(myfont_body.render("Main Menu", 1, THECOLORS['antiquewhite']), (345,505))

def lesson_button():
    pygame.draw.rect(screen, THECOLORS['brown'], (530, 500, 170, 50))
    screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (565,505))
def restart_button():
    pygame.draw.rect(screen, THECOLORS['brown'], (130, 500, 170, 50))
    screen.blit(myfont_body.render("Restart", 1, THECOLORS['antiquewhite']), (170,505))

        
# The Game Loop
running=True
show="ending 1"
try:
    while running:
        clock.tick(60)
        #to scroll through the endings, press the space bar!!
        if show == "ending 1":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake bite", 1, THECOLORS['antiquewhite']), (300,170))

            #death description
            x=125
            y=210
            with open("textFiles/ending 1.txt") as word_file:
                for sentence in word_file:
                    y+=30
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()
            
        elif show =="ending 2":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake bite", 1, THECOLORS['antiquewhite']), (300,170))

            #death description
            x=125
            y=210
            with open("textFiles/ending 2.txt") as word_file:
                for sentence in word_file:
                    y+=30
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()

            
        elif show == "ending 3a":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake attack", 1, THECOLORS['antiquewhite']), (300,170))
            
            #death description
            x=120
            y=220
            with open("textFiles/ending 3a.txt") as word_file:
                for sentence in word_file:
                    y+=30
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()
        elif show =="ending 3b":
            surface = pygame.image.load("images/death.png")
            screen.blit(surface,(0,0))
            #cause of death
            screen.blit(myfont_body.render("Snake attack", 1, THECOLORS['antiquewhite']), (300,170))
            
            #death description
            x=120
            y=210
            with open("textFiles/ending 3b.txt") as word_file:
                for sentence in word_file:
                    y+=28
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()
            
        elif show =="ending 4":
            surface = pygame.image.load("images/treasure.png")
            screen.blit(surface,(0,0))
            #Success!
            screen.blit(myfont_title.render("You made it!", 1, THECOLORS['antiquewhite']), (275,75))

            #some praise
            screen.blit(myfont_body.render("You have successfully completed your missions!", 1, THECOLORS['antiquewhite']), (135,250))
            screen.blit(myfont_body.render("Now you live a comfortable and wealthy life!", 1, THECOLORS['antiquewhite']), (160,325))
            pygame.display.flip()

        #do not add this part to main program! this code is only to scroll through the endings.
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
