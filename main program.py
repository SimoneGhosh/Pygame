"""
Author: Simone
Date: 2021-12-27
Name: main_program
Description: Combine the title screen and main menu
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
pygame.display.set_caption('Poisonous Pyramids') 
screen = pygame.display.get_surface() 

#Change the logo of our window
pygame_icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(pygame_icon)

#Clock
clock = pygame.time.Clock()
refresh_rate=30

#Adding music
# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("music/music.wav")
# Setting the volume
mixer.music.set_volume(0.3)
# Start playing the song
mixer.music.play()

#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
test=pygame.display.get_driver()


#Title screen
surface = pygame.image.load("images/bluebg.jpg")
screen.blit(surface,(0,0))

#Displaying title
text=myfont_title.render("POISONOUS", True, THECOLORS["brown"])
text2=myfont_title.render("PYRAMIDS", True, THECOLORS["brown"])
screen.blit(text, (175,50))
screen.blit(text2, (225,150))

#Update and refresh the display to end this frame
pygame.display.flip() #flip all changes onto the display window
time.sleep(1) #<-- Window will pause and than change 



# The Game Loop
running=True
show="main menu"

try:
    while running:
        #The Event Loop #
        events=pygame.event.get()
        clock.tick(60) #frame rate/second
        
        #Main menu/background image        
        surface = pygame.image.load("images\pyramids.jpg")
        screen.blit(surface,(0,0))
        
        #Displaying titles 
        title=myfont_title.render("POISONOUS", True, THECOLORS["brown"])
        title_end=myfont_title.render("PYRAMIDS", True, THECOLORS["brown"])
        sub_title=myfont_body.render("main menu", True, THECOLORS["brown"])
        
        screen.blit(title, (175,50))
        screen.blit(title_end, (225,125))
        screen.blit(sub_title, (350,200))        
        
        #Depending on which show is used, show a different screen and buttons
        if show == "main menu":
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
        
        elif show == "instructions":
            screen.fill(THECOLORS["red"])
            #Button to return to main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (732,555))
            
        elif show == "lesson":
            screen.fill(THECOLORS["orange"])
            #Button to return to main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (732,555))            
        
        elif show == "review":
            screen.fill(THECOLORS["yellow"])
            #Button to return to main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (732,555))
            
        elif show == "quiz":
            screen.fill(THECOLORS["pink"])
            #Button to return to main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (732,555))
            
        #Allow user to exit the game
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            
            # Detecting the click inside the button area
            if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="main menu":
                show = "instructions"
            elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1 and show=="main menu":
                show = "lesson"            
            elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1 and show=="main menu":
                show = "review"    
            elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1 and show=="main menu":
                show = "quiz"             
            elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and (show=="instructions" or show=="lesson" or show=="review" or show=="quiz"):
                show = "main menu"
                
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                x=0
                y=0
                credit_screen= pygame.image.load("images/roll_credits.png").convert_alpha()                
                
                #scroll
                while y!=-600:
                    y-=5
                    screen.blit(credit_screen,(x, y))
                    pygame.display.flip()	 #update screen
                    clock.tick(refresh_rate)
                running=False    

        pygame.display.update()
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly