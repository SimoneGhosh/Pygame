"""
Author: Mona
Date: Jan 7, 2021
Name: lesson
Description: Will teach the user the content about Ancient Egypt!
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
'''
#Adding music
# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("music/music.wav")
# Setting the volume
mixer.music.set_volume(0.3)
# Start playing the song
mixer.music.play()
'''

#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
myfont_medium = pygame.font.SysFont("times new roman", 22)
test=pygame.display.get_driver()
lesson_font_big = pygame.font.SysFont("Papyrus", 75)



def next_button():    
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (720, 525, 100, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (725, 530, 90, 50))
    screen.blit(myfont_body.render("NEXT", 1, THECOLORS['antiquewhite']), (730,538))
    pygame.display.flip()





# The Game Loop
running=True
show="lesson"
quiz_completed = False
try:
    while running:
        clock.tick(60) #frame rate/second

        if show == "lesson":
            
            #first screen background
            lesson_screen = pygame.image.load("images/lesson_background.png")
            screen.blit(lesson_screen,(0,0))

            
            

            screen.blit(lesson_font_big.render("LESSON", 1, THECOLORS['antiquewhite']), (315,50))
           
            x=50
            y=160
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (40, 150, 700, 120))
            with open("textFiles/lessonintro.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40

            pygame.draw.rect(screen, THECOLORS['brown'], (300, 300, 300, 100))
            screen.blit(myfont_title.render("START", 1, THECOLORS['antiquewhite']), (365,305))
            
            pygame.display.flip()
        

        elif show=="lesson 1":
        
            surface = pygame.image.load("images/lesson_screen_1.png")
            screen.blit(surface,(0,0))
            #images
            '''
            nile = pygame.image.load("images/nile river.jpeg")
            screen.blit(nile,(50,25))
            '''


            
            x=50
            y=160
            with open("textFiles/lesson_1_quick_geography.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))


            
            next_button()
            pygame.display.flip()

        elif show == "lesson 2":
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            x=50
            y=160
            with open("textFiles/Lesson_2_egyptian_rule.txt") as word_file:
                for sentence in word_file:
                    y+=60
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button()
            pygame.display.flip()

 

        # The Event Loop #
        events=pygame.event.get()
            
        #Allow user to click buttons
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            
            
            
           
            #lesson buttons
            #start button
            if x>300 and x<300+300 and y>300 and y<300+100 and butt[0]==1 and show=="lesson":
                show = "lesson 1"
            #next button to lesson 2
            if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1 and show=="lesson":
                show = "lesson 2"             
            
            #Exit    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                x=0
                y=0
                credit_screen=pygame.image.load("images/roll_credits.png").convert_alpha()                
                
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
