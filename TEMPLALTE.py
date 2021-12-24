#TEMPLATE
#import modules
import pygame
from pygame.locals import *  
from pygame.color import THECOLORS   #can use colour names instead of hexidecimal
import os, time

#initialize library
pygame.init()

#to work on tdsb computer 
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
#create screen
screen=pygame.display.set_mode((850, 600))

#Make Game title and icon
pygame.display.set_caption("Poisonous Pyramid")
icon= pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#set fonts
myfont = pygame.font.SysFont("Papyrus", 50)     #using different font sizes
mysmallfont = pygame.font.SysFont("Papyrus", 25)

#add image
sphinximg= pygame.image.load("greatSphinx.png")
sphinximgX=100#coordinates
sphinximgY=100
def sphinx():
    screen.blit(sphinximg, (sphinximgX, sphinximgY)) 

clock = pygame.time.Clock() #clock

#Game Loop
keep_running=True

while keep_running:
    clock.tick(60) #frame rate /second
    screen.fill((0, 200, 0))        #background colour/ background
    
    for event in pygame.event.get(): #checks through all events
        if event.type==pygame.QUIT:
            running = False #shuts fown game loop once exit is pressed
    #adds text    
    text=myfont.render("Credits", True, THECOLORS["black"])
    screen.blit(text,(370,50))
    credits1=mysmallfont.render("book", True, THECOLORS["black"])
    screen.blit(credits1,(390,125))
    
    sphinx()#CALL IMAGE
    
    pygame.display.update()	 #update screen


        
            
    
    
