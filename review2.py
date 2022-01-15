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

counter=13
text = myfont_title.render(str(counter), True, (THECOLORS['antiquewhite']))  
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000) 

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
            time.sleep(1)
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
        
        elif show == "question 2":
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
                    y+=30
                    screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            
            text_rect = text.get_rect(center = window.get_rect().center)
            window.blit(text, text_rect)
            pygame.display.flip()            
            
            match = pygame.image.load("images/match.png")
            screen.blit(match,(765,175)) 
         
            pygame.display.flip()
        
        elif show == "question 3":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))      
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("The flooding of the Nile river occured", 1, THECOLORS['antiquewhite']), (180,155))
            screen.blit(myfont_body.render("_______.", 1, THECOLORS['antiquewhite']), (350,200))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 200, 50))
            screen.blit(myfont_body.render("Quarterly", 1, THECOLORS['antiquewhite']), (215,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (450, 300, 200, 50))
            screen.blit(myfont_body.render("Semiannually", 1, THECOLORS['antiquewhite']), (470,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 200, 50))
            screen.blit(myfont_body.render("Monthly", 1, THECOLORS['antiquewhite']), (225,410)) 
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (450, 400, 200, 50))
            screen.blit(myfont_body.render("Annually", 1, THECOLORS['antiquewhite']), (500,410))             
        
        elif show == "question 4":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))      
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Which time period are you in right", 1, THECOLORS['antiquewhite']), (200,155))
            screen.blit(myfont_body.render("now? (1400 BCE)", 1, THECOLORS['antiquewhite']), (300,200))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 200, 50))
            screen.blit(myfont_body.render("Mesozoic", 1, THECOLORS['antiquewhite']), (220,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (450, 300, 200, 50))
            screen.blit(myfont_body.render("New kingdom", 1, THECOLORS['antiquewhite']), (470,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 200, 50))
            screen.blit(myfont_body.render("Old kingdom", 1, THECOLORS['antiquewhite']), (200,410)) 
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (450, 400, 200, 50))
            screen.blit(myfont_body.render("Aegyptus", 1, THECOLORS['antiquewhite']), (495,410))               
        
        
        elif show == "drink eat sleep":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))    
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 100, 475, 100))
            screen.blit(myfont_body.render("You are hungry, thirsty, and sleepy.", 1, THECOLORS['antiquewhite']), (200,110))
            screen.blit(myfont_body.render("What do you do?", 1, THECOLORS['antiquewhite']), (315,160))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 250, 475, 50))
            screen.blit(myfont_body.render("Drink some water.", 1, THECOLORS['antiquewhite']), (305,260))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 475, 50))
            screen.blit(myfont_body.render("Eat a delicious snack.", 1, THECOLORS['antiquewhite']), (290,360))             
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 450, 475, 50))
            screen.blit(myfont_body.render("Take a quick nap.", 1, THECOLORS['antiquewhite']), (305,460))             
        
        elif show == "question 5":
            surface = pygame.image.load("images/pyramids_img.jpg")
            screen.blit(surface,(0,0))               
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Approximately, how many gods did", 1, THECOLORS['antiquewhite']), (195,155))
            screen.blit(myfont_body.render("the ancient Egyptians worship?", 1, THECOLORS['antiquewhite']), (220,200))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("1500", 1, THECOLORS['antiquewhite']), (215,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("88", 1, THECOLORS['antiquewhite']), (560,305))
    
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("2000", 1, THECOLORS['antiquewhite']), (215,410)) 
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("3000", 1, THECOLORS['antiquewhite']), (540,410))            
            
        """
        elif show == "ending 1":
        
        elif show == "ending 2":
        
        elif show == "ending 3a":
        
        elif show == "ending 3b":
        
        elif show=="ending 4"
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
                    show="question 2"
                    path_taken=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="question 2"                 
            
            elif show=="question 2":
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
            
            elif show=="find match":
                if x>765 and x<765+24 and y>175 and y<175+24 and butt[0]==1:
                    show="question 3"
                elif event.type == timer_event:
                    counter -= 1
                    text = myfont_title.render(str(counter), True, (THECOLORS["antiquewhite"]))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)  
                        show="question 3"                
            
            elif show=="question 3":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="question 4"          
                    
            elif show=="question 4":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="drink eat sleep"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"                     
                    
            elif show=="drink eat sleep":
                if x>175 and x<175+475 and y>250 and y<250+50 and butt[0]==1:
                    show="question 5"
                elif x>175 and x<175+475 and y>350 and y<350+50 and butt[0]==1:
                    show="ending 3b"
                elif x>175 and x<175+475 and y>450 and y<450+50 and butt[0]==1:
                    show="ending 3a"
                    
            elif show=="question 5":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 4"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"     
                    
            #Allowing user to quit program    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                running = False        
            
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly