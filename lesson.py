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
myfont_special=pygame.font.SysFont("Papyrus", 40)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
myfont_medium = pygame.font.SysFont("times new roman", 22)
test=pygame.display.get_driver()
lesson_font_big = pygame.font.SysFont("Papyrus", 75)



def next_button_back_button():    
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (720, 525, 100, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (725, 530, 90, 50))
    screen.blit(myfont_body.render("NEXT", 1, THECOLORS['antiquewhite']), (730,538))
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (610, 525, 100, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (615, 530, 90, 50))
    screen.blit(myfont_body.render("BACK", 1, THECOLORS['antiquewhite']), (620,538))
    



# The Game Loop
running=True
show="lesson"
try:
    while running:
        clock.tick(60) #frame rate/second

        if show == "lesson":
            
            #first screen background
            lesson_screen = pygame.image.load("images/lesson_background.png")
            screen.blit(lesson_screen,(0,0))

            screen.blit(lesson_font_big.render("LESSON", 1, THECOLORS['antiquewhite']), (315,50))
           
            x=45
            y=160
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (40, 150, 770, 120))
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (40, 275, 225, 200))
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (600, 300, 210, 170))
            with open("textFiles/lessonintro.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40

            #start button------
     
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (295, 295, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (300, 300, 275, 100))   
            screen.blit(myfont_title.render("START", 1, THECOLORS['antiquewhite']), (365,312))
            #-----------------------

            #UNIT BUTTONS
            #lesson 1
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (10, 485, 158, 95))
            pygame.draw.rect(screen, THECOLORS['brown'], (15, 490, 148, 85))   
            screen.blit(myfont_body.render("Unit 1", 1, THECOLORS['antiquewhite']), (46, 500))
            screen.blit(myfont_medium.render("Geography", 1, THECOLORS['antiquewhite']), (38,535))
            #lesson 2

            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (178, 485, 158, 95))
            pygame.draw.rect(screen, THECOLORS['brown'], (183, 490, 148, 85))   
            screen.blit(myfont_body.render("Unit 2", 1, THECOLORS['antiquewhite']), (218,500))
            screen.blit(myfont_medium.render("Egyptian Rule", 1, THECOLORS['antiquewhite']), (197,535))

            #lesson 3
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (346, 485, 158, 95))
            pygame.draw.rect(screen, THECOLORS['brown'], (351, 490, 148, 85))   
            screen.blit(myfont_body.render("Unit 3", 1, THECOLORS['antiquewhite']), (383,500))
            screen.blit(myfont_medium.render("Old Kingdom", 1, THECOLORS['antiquewhite']), (363,535))

            #lesson 4
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (514, 485, 158, 95))
            pygame.draw.rect(screen, THECOLORS['brown'], (519, 490, 148, 85))   
            screen.blit(myfont_body.render("Unit 4", 1, THECOLORS['antiquewhite']), (554,500))
            screen.blit(myfont_medium.render("The Arts", 1, THECOLORS['antiquewhite']), (555,535))

            #lesson 5
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (682, 485, 158, 95))
            pygame.draw.rect(screen, THECOLORS['brown'], (687, 490, 148, 85))   
            screen.blit(myfont_body.render("Unit 5", 1, THECOLORS['antiquewhite']), (722,500))
            screen.blit(myfont_medium.render("Materials", 1, THECOLORS['antiquewhite']), (720,535))
            


        
            pygame.display.flip()
        

        elif show=="lesson 1":
        
            surface = pygame.image.load("images/lesson_screen_1.png")
            screen.blit(surface,(0,0))
            screen.blit(lesson_font_big.render("1. Geography", 1, THECOLORS['antiquewhite']), (315,50))
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


            next_button_back_button()
            pygame.display.flip()

        elif show=="lesson 2":
              
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_title.render("2. Timeline ", 1, THECOLORS['antiquewhite']), (250,50))
            x=50
            y=85
            with open("textFiles/Lesson_2_egyptian_rule.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()

        elif show=="lesson 3":
        
            surface = pygame.image.load("images/lesson_screen_1.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_title.render("3.The Old Kingdom ", 1, THECOLORS['antiquewhite']), (315,50))
            #text
            x=50
            y=160
            with open("textFiles/lesson_3_the_old_kingdom.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()

        elif show=="lesson 4":
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_special.render("4. The Middle Kingdom and The Arts", 1, THECOLORS['antiquewhite']), (50,50))
            x=50
            y=70
            with open("textFiles/lesson_4_the_middle_kingdom.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()
            
        elif show=="lesson 5":
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_special.render("5. What did they write on?", 1, THECOLORS['antiquewhite']), (100,50))
            x=50
            y=75
            with open("textFiles/seperate_but_what_did_they_write_on.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))

            #done button
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (720, 525, 100, 60))
            pygame.draw.rect(screen, THECOLORS['brown'], (725, 530, 90, 50))
            screen.blit(myfont_body.render("DONE", 1, THECOLORS['antiquewhite']), (730,538))
            #back button
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (610, 525, 100, 60))
            pygame.draw.rect(screen, THECOLORS['brown'], (615, 530, 90, 50))
            screen.blit(myfont_body.render("BACK", 1, THECOLORS['antiquewhite']), (620,538))
    

            pygame.display.flip()
            
        elif show=="done":
            lesson_screen = pygame.image.load("images/lesson_background.png")
            screen.blit(lesson_screen,(0,0))

            screen.blit(lesson_font_big.render("END OF LESSON!", 1, THECOLORS['antiquewhite']), (100,50))
           
            x=50
            y=180
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (40, 160, 250, 375))
            with open("textFiles/done.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40

                    
            #main menu
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (495, 150, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 155, 275, 100))   
            screen.blit(myfont_title.render("Main menu", 1, THECOLORS['antiquewhite']), (515,155))

            #back to start
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (495, 295, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 275, 100))   
            screen.blit(myfont_special.render("Back to start", 1, THECOLORS['antiquewhite']), (515,325))

        
            pygame.display.flip()


 

        # The Event Loop #
        events=pygame.event.get()
            
        #Allow user to click buttons
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    show = "lesson"
           
            #lesson buttons
            
            if show == "lesson": #from lesson page
                #start button
                if x>300 and x<300+300 and y>300 and y<300+100 and butt[0]==1:
                    show = "lesson 1"
                #UNIT BUTTONS
                #to lesson 1
                elif x>10 and x<10+158 and y>485 and y<485+95 and butt[0]==1:
                    show = "lesson 1"
                #to lesson 2
                elif x>178 and x<178+158 and y>485 and y<485+95 and butt[0]==1:
                    show = "lesson 2"
                #to lesson 3
                elif x>346 and x<346+158 and y>485 and y<485+95 and butt[0]==1:
                    show = "lesson 3"
                #to lesson 4
                elif x>514 and x<514+158 and y>485 and y<485+95 and butt[0]==1:
                    show = "lesson 4"
                #to lesson 5
                elif x>682 and x<682+158 and y>485 and y<485+95 and butt[0]==1:
                    show = "lesson 5"

                

                
            #NEXT AND BACK 
            elif show=="lesson 1":
                #next button to lesson 2
                if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1:
                    show = "lesson 2"
                #back button to lesson start page
                elif x>610 and x<610+100 and y>525 and y<525+60 and butt[0]==1:
                    show="lesson"

    
            
            elif show=="lesson 2":
                #next button to lesson 3
                if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1:
                    show = "lesson 3"
                #back button to lesson 1
                elif x>610 and x<610+100 and y>525 and y<525+60 and butt[0]==1:
                    show="lesson 1"

            
            elif show=="lesson 3":
                #next button to lesson 4
                if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1:
                    show = "lesson 4"
                #back button to lesson 2
                elif x>610 and x<610+100 and y>525 and y<525+60 and butt[0]==1:
                    show="lesson 2"
           
            elif show=="lesson 4":
                #next button to lesson 5
                if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1:
                    show = "lesson 5"
                #back button to lesson 3
                elif x>610 and x<610+100 and y>525 and y<525+60 and butt[0]==1:
                    show="lesson 3"

            elif show=="lesson 5":
                #next button to lesson done
                if x>720 and x<720+100 and y>525 and y<525+60 and butt[0]==1:
                    show = "done"
                #back button to lesson 4
                elif x>610 and x<610+100 and y>525 and y<525+60 and butt[0]==1:
                    show="lesson 4"
                    
            elif show=="done":
                '''
                #go to main menu
                if x>495 and x<495+285 and y>150 and y<150+110 and butt[0]==1:
                    show = "main menu"
                '''
                #go to start of lesson
                # change following if to elif in main program
        
                if x>495 and x<495+285 and y>295 and y<295+110 and butt[0]==1:
                    show="lesson"
        
            #Exit    
            elif(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
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
