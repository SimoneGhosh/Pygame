"""
Author: Simone and Mona
Date: 2021-12-30
Name: Ineractive review 
Description: The user goes on a mission to look for a treaure chest and has to
complete knowlege questions. If the user answers wrong, their character will die
and they will be given the options to return to the main menu, restart, or go to lesson.
"""

#Import modules

import pygame, sys, os, time
from pygame.locals import * 
from pygame.color import THECOLORS
from pygame import mixer

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
myfont_medium= pygame.font.SysFont("times new roman", 23)#######add this font to main!
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
    
def main_menu_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (325, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (330, 500, 170, 50))
    screen.blit(myfont_body.render("Main Menu", 1, THECOLORS['antiquewhite']), (345,505))

def lesson_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (525, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (530, 500, 170, 50))
    screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (565,505))
    
def restart_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (125, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (130, 500, 170, 50))
    screen.blit(myfont_body.render("Restart", 1, THECOLORS['antiquewhite']), (170,505))
        
# The Game Loop
running=True
show="review"

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
                for i in range(9):
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
            
            ready = False
            path_taken = False
            screen_black = False            
            
        elif show == "answering Q1":
            surface = pygame.image.load("images/pyramid.jpg")
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
            
        elif show == "map 1":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            if path_taken:
                x=124
                while x<468:
                    x+=1
                    screen.blit(marker,(x,35))
                    pygame.display.flip()
                    screen.blit(surface,(0,0)) 
                
            else:
                x=124
                y=35
                while x<207:
                    x+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))
                while y<115:
                    y+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0)) 
                while x<422:
                    x+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))                     
                while y>75:
                    y-=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))  
                while x<505:
                    x+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))    
            
            time.sleep(1)
            show="question 2"    
            pygame.display.flip()

        elif show == "question 2":
            surface = pygame.image.load("images/split path.png")
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
        
        elif show=="map 2":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            if path_taken:         
                x=468
                y=35
                while x<550:
                    x+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0)) 
                while y<156:
                    y+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))                                    
            else:
                x=505
                y=75
                while y>34:
                    y-=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))
                while x<550:
                    x+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0)) 
                while y<156:
                    y+=1
                    screen.blit(marker,(x,y))
                    pygame.display.flip()
                    screen.blit(surface,(0,0))  
  
            time.sleep(1)
            
            counter = 14
            text = myfont_title.render(str(counter), True, (THECOLORS['antiquewhite']))
            timer_event = pygame.USEREVENT+1
            pygame.time.set_timer(timer_event, 1000)
            
            show="find match"    
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
            if counter<=10:
                window.blit(text, text_rect)
            
            match = pygame.image.load("images/match.png")
            screen.blit(match,(765,175)) 
         
            pygame.display.flip()
        
        elif show=="map 3":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            x=550
            y=156
            while x>85:
                x-=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0)) 
            while y<280:
                y+=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0))
            while x<290:
                x+=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0))                 
  
            time.sleep(1)
            show="question 3"    
            pygame.display.flip()
            
        elif show == "question 3":
            surface = pygame.image.load("images/tunnel1.jpg")
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
        
        elif show=="map 4":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            x=290
            y=280
            while x<592:
                x+=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0)) 
            time.sleep(1)
            show="question 4"    
            pygame.display.flip()
        
        elif show == "question 4":
            surface = pygame.image.load("images/tunnel2.jpg")
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
        
        elif show=="map 5":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            x=592
            y=280
            while x<717:
                x+=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0)) 
            while y<400:
                y+=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0)) 
            while x>590:
                x-=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0))                 
            time.sleep(1)
            show="drink eat sleep"    
            pygame.display.flip()            
        
        elif show == "drink eat sleep":
            surface = pygame.image.load("images/tunnel3.jpg")
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
        
        elif show=="map 6":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            x=590
            y=400
            while x>365:
                x-=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0))            
            time.sleep(1)
            show="question 5"    
            pygame.display.flip()
            
        elif show == "question 5":
            surface = pygame.image.load("images/tunnel4.jpg")
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
            
        elif show=="map 7":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            x=365
            y=400
            while x>195:
                x-=1
                screen.blit(marker,(x,y))
                pygame.display.flip()
                screen.blit(surface,(0,0))            
            time.sleep(1)
            show="ending 4"    
            pygame.display.flip()

        #ENDINGS-------------------------------------------------------------------------------
        elif show == "ending 1":
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
            
        elif show == "ending 2":
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
            
        elif show == "ending 3b":
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
            
        elif show=="ending 4":
            surface = pygame.image.load("images/treasure.png")
            screen.blit(surface,(0,0))
            #Success!
            screen.blit(myfont_title.render("YOU MADE IT!", 1, THECOLORS['antiquewhite']), (160,75))

            #some praise
            screen.blit(myfont_body.render("You have successfully completed your missions!", 1, THECOLORS['black']), (135,250))
            screen.blit(myfont_body.render("Now you live a comfortable and wealthy life!", 1, THECOLORS['black']), (135,300))
            screen.blit(myfont_body.render("You are even prepared to complete the quiz", 1, THECOLORS['black']), (135,350))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (130, 500, 170, 50))
            screen.blit(myfont_body.render("Main Menu", 1, THECOLORS['antiquewhite']), (145,505))       
            
            pygame.draw.rect(screen, THECOLORS['brown'], (530, 500, 170, 50))
            screen.blit(myfont_body.render("Quiz", 1, THECOLORS['antiquewhite']), (590,505))
            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()
        
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
                    show="map 1"
                    path_taken=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="map 1"                 
            
            elif show=="question 2":
                if path_taken:
                    if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                        show="map 2"
                        
                    elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                        show="ending 1"     
                else:
                    if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                        show="ending 1"     
                    elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                        show="ending 1"     
                    elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                        show="map 2"
                    elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                        show="ending 1"     
            
            elif show=="find match":
                if x>765 and x<765+24 and y>175 and y<175+24 and butt[0]==1:
                    show="map 3"
                elif event.type == timer_event:
                    counter -= 1
                    text = myfont_title.render(str(counter), True, (THECOLORS["antiquewhite"]))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)  
                        show="ending 2"                
            
            elif show=="question 3":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="map 4"          
                    
            elif show=="question 4":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="map 5"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"                     
                    
            elif show=="drink eat sleep":
                if x>175 and x<175+475 and y>250 and y<250+50 and butt[0]==1:
                    show="map 6"
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
                    show="map 7"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"     
            
            elif show=="ending 1" or show=="ending 2" or show=="ending 3a" or show=="ending 3b" or show=="ending 4":
                if x>330 and x<330+170 and y>500 and y<500+50 and butt[0]==1:
                    show="main menu"
                elif x>530 and x<330+170 and y>500 and y<500+50 and butt[0]==1:
                    show="lesson"
                elif x>130 and x<330+170 and y>500 and y<500+50 and butt[0]==1:
                    show="review"
            
            
                



                 
            #Allowing user to quit program    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                running = False        
            
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly
