'''
author: Mona and Simone
Date: December 23, 2021
Name: Credits
Description: Roll credits before quit
'''

#import modules
import pygame
from pygame.locals import *  
from pygame.color import THECOLORS   #can use colour names instead of hexidecimal
import os, time
# initial library itself
pygame.init()  


#to work on tdsb computer 
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Set-up the main screen display window and caption  in the 
size = (850,600)  
screen = pygame.display.set_mode(size)
pygame.display.set_caption("poisonous pyramids")
surface = pygame.image.load("images/creditssurface.jpeg")
screen.blit(surface,(0,0))


clock = pygame.time.Clock() #clock
keepGoing = True 	     
myfont = pygame.font.SysFont("Papyrus", 50)     #using different font sizes
mysmallfont = pygame.font.SysFont("Papyrus", 25)
test=pygame.display.get_driver()
try:
    while keepGoing:
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second  
        text=myfont.render("Credits", True, THECOLORS["black"])
        screen.blit(text,(370,50))
        credits1=mysmallfont.render("book", True, THECOLORS["black"])
        screen.blit(credits1,(390,125))

           # Place (or blit) text on certain location (x, y) of the screen
        pygame.display.flip()
        #Handle any events in the current frame
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                keepGoing = False
finally:
    pygame.quit()  # Keep this IDLE friendly
    

