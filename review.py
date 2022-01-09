"""
Author: Simone
Date: 2021-12-30
Name: quiz
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

#This code is necessary for python to work on tdsb computers
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Clock
clock = pygame.time.Clock()
refresh_rate=30

#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
test=pygame.display.get_driver()

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(surface,(0,0))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
        
        if alpha==300:
            break
        
# The Game Loop
running=True
show="review"
ready = False
path_taken = False
screen_black = False
try:
    while running:
        clock.tick(60)
        
        if show == "review":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))
            
            #Displaying titles 
            title=myfont_title.render("REVIEW", True, THECOLORS["brown"])
            screen.blit(title, (275,50))
            
            #Display a speech
            x=180
            y=135
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 185))
            with open("textFiles/review info.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_small.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            
            #Button to lesson
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
            screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (205,360)) 
            
            #Button for main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (335, 350, 150, 50))
            screen.blit(myfont_body.render("Main menu", 1, THECOLORS['antiquewhite']), (340,360))
            
            #Button to begin quiz
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
            screen.blit(myfont_body.render("Start", 1, THECOLORS['antiquewhite']), (545,360))        
            
        elif show == "answering Q1":
            screen.blit(surface,(0,0))
            
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Hieroglyphs are a form of", 1, THECOLORS['antiquewhite']), (250,155))
            screen.blit(myfont_body.render("communication.", 1, THECOLORS['antiquewhite']), (300,205))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 475, 50))
            screen.blit(myfont_body.render("True", 1, THECOLORS['antiquewhite']), (390,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 475, 50))
            screen.blit(myfont_body.render("False", 1, THECOLORS['antiquewhite']), (385,410)) 

            pygame.display.flip()           
        
        elif show == "answered Q1":
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 475, 50))
            screen.blit(myfont_body.render("True", 1, THECOLORS['black']), (390,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 475, 50))
            screen.blit(myfont_body.render("False", 1, THECOLORS['antiquewhite']), (385,410)) 
            
            pygame.display.flip()
            time.sleep(2)
            show="prepared"             
            
        elif show == "prepared":
            if ready:
                show = "hidden path"
            
            else:
                screen.blit(surface,(0,0))
                
                #Display a speech
                x=180
                y=135
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 185))
                with open("textFiles/review info.txt") as word_file:
                    for sentence in word_file:
                        y+=20
                        screen.blit(myfont_small.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                
                #Button to lesson
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
                screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (205,360)) 
                
                #Button for main menu
                pygame.draw.rect(screen, THECOLORS['brown'], (335, 350, 150, 50))
                screen.blit(myfont_body.render("Main menu", 1, THECOLORS['antiquewhite']), (340,360))
                
                #Button to begin quiz
                pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
                screen.blit(myfont_body.render("Continue", 1, THECOLORS['antiquewhite']), (525,360))                  
            
            pygame.display.flip()               
        
        elif show == "hidden path":
            surface = pygame.image.load("images/split path.png")
            screen.blit(surface,(0,0))
            
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 50, 475, 210))
            screen.blit(myfont_body.render("There is a hidden path, a shortcut.", 1, THECOLORS['antiquewhite']), (180,55))
            screen.blit(myfont_body.render("Do you want to take it? Make the", 1, THECOLORS['antiquewhite']), (180,105))
            screen.blit(myfont_body.render("wrong choice, and your life will be", 1, THECOLORS['antiquewhite']), (180,155))
            screen.blit(myfont_body.render("will be at stake.", 1, THECOLORS['antiquewhite']), (180,205))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 475, 50))
            screen.blit(myfont_body.render("Yes, I will take the short cut.", 1, THECOLORS['antiquewhite']), (235,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 475, 50))
            screen.blit(myfont_body.render("No, I will continue on my path.", 1, THECOLORS['antiquewhite']), (215,410)) 

            pygame.display.flip()             
        
        elif show == "answering Q2":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))
            
            if path_taken:
                #Question
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
                screen.blit(myfont_body.render("The Nile River is the longest river in", 1, THECOLORS['antiquewhite']), (190,155))
                screen.blit(myfont_body.render("the world.", 1, THECOLORS['antiquewhite']), (365,205))
                
                #Button for answer
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 475, 50))
                screen.blit(myfont_body.render("True", 1, THECOLORS['antiquewhite']), (390,305))
            
                #Button for answer
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 475, 50))
                screen.blit(myfont_body.render("False", 1, THECOLORS['antiquewhite']), (385,410)) 
            else:
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
                screen.blit(myfont_body.render("Who was Egypt’s first Pharaoh?", 1, THECOLORS['antiquewhite']), (225,180))
                
                #Button for answer
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
                screen.blit(myfont_body.render("Djoser", 1, THECOLORS['antiquewhite']), (210,305))
        
                #Button for correct answer
                pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
                screen.blit(myfont_body.render("Khufu", 1, THECOLORS['antiquewhite']), (535,305))
        
                #Button for correct answer
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
                screen.blit(myfont_body.render("Menes", 1, THECOLORS['antiquewhite']), (210,410)) 
                
                #Button for answer
                pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
                screen.blit(myfont_body.render("Ramses II", 1, THECOLORS['antiquewhite']), (515,410))                 
    
            pygame.display.flip()                 
        
            
        elif show == "find match":
            surface = pygame.image.load("images/split path.png")
            screen.blit(surface,(0,0))
            
            if not(screen_black):
                fade(850, 600)
                screen_black = True
                
            screen.fill(THECOLORS["black"])
            
            #Display a speech
            x=5
            y=-15
            with open("textFiles/find match.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    
            
            match = pygame.image.load("images/match.png")
            screen.blit(match,(765,175)) 
         
            pygame.display.flip()
        
        elif show == "answering Q3":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))            
        """
        elif show == "answered Q2":
        
        elif show == "answering Q3":
        
        elif show == "answered Q3":
        
        elif show == "eat sleep drink":
        
        elif show == "answering Q4":
        
        elif show == "ending 1":
        
        elif show == "ending 2":
        
        elif show == "ending 3a":
        
        elif show == "ending 3b":
        """    
        # The Event Loop #
        events=pygame.event.get()
            
        #Allow user to exit the game
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            
        # Detecting the click inside the button area
            #quiz
            #Quiz buttons
            if show=="review":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"                
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                    show="answering Q1"
            
            elif show=="answering Q1": 
                if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q1"
                    ready=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q1"    
            
            elif show=="prepared":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"                
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                    show="hidden path"                
            
            elif show=="hidden path":
                if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                    show="answering Q2"
                    path_taken=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="answering Q2"                 
            
            elif show=="answering Q2":
                if path_taken:
                    if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                        show="find match"
                    elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                        show="ending 1"     
                else:
                    if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                        show="ending 1"     
                    elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                        show="ending 1"     
                    elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                        show="find match"
                    elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                        show="ending 1"     
            
            if show=="find match":
                if x>765 and x<765+15 and y>175 and y<175+15 and butt[0]==1:
                    show="answering Q3"
                    
                    
            #Allowing user to quit program    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                running = False        
            
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly