
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
icon= pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
#clock
clock = pygame.time.Clock() 
refresh_rate=30



#image
#add image
credit_screen= pygame.image.load("images/roll_creds.png").convert_alpha()
#initialize coordinates
'''
sphinximgX=0
sphinximgY=0
'''
'''
def sphinx():
    screen.blit(sphinximg, (sphinximgX, sphinximgY))
'''
x=0
y=0
keep_running=True

while keep_running:
    clock.tick(60) #frame rate /second
    for event in pygame.event.get(): #checks through all events
        if event.type==pygame.QUIT:
            running = False #shuts fown game loop once exit is pressed
    #scroll
    y-=5       
    screen.blit(credit_screen,(x, y))
    if y==-600:
        keep_running=False
    pygame.display.flip()	 #update screen
    clock.tick(refresh_rate)
    
