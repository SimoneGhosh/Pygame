"""
Author: Simone and Mona
Date: 2022-01-18
Name: Poisonous_pyramid
Description: Completed program
"""

#Import modules----------------------------------------------------------------------------------------
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

#Initial library itself---------------------------
pygame.init() 


#Set-up the main screen display window-----------------------------------------------------------------
size = (850,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Poisonous Pyramid') 
screen = pygame.display.get_surface() 

#Change the logo of our window--------------------
pygame_icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(pygame_icon)

#Clock---------------------------------------------
clock = pygame.time.Clock()
refresh_rate=30

#Adding music--------------------------------------
# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("music/music.wav")
# Setting the volume
mixer.music.set_volume(0.3)
# Start playing the song
mixer.music.play(-1) #<-- -1 plays music in a loop

#Setting up the font and the size-------------------------
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
myfont_small = pygame.font.SysFont("times new roman", 15)
myfont_special=pygame.font.SysFont("Papyrus", 40)
myfont_medium = pygame.font.SysFont("times new roman", 22)
lesson_font_big = pygame.font.SysFont("Papyrus", 75)
test=pygame.display.get_driver()


#Procedures and functions------------------------------------------------------------------------------
#Procedure to display quiz button-------------------------
def question():
    screen.blit(surface,(0,0))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
    
#Procedure to display sentences---------------------------
def phrase(font, answer, colour, width, length):
    screen.blit(font.render(answer, 1, THECOLORS[colour]), (width,length))
        
#Procedures to display quiz score-------------------------
def score(correct_answers):
    pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
    screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))

#Procedure to display buttons-----------------------------
def button(colour, x_value, y_value, width, length):
    pygame.draw.rect(screen, THECOLORS[colour], (x_value, y_value, width, length))

#Procedure to display next and back buttons for lesson----
def next_button_back_button():    
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (720, 525, 100, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (725, 530, 90, 50))
    screen.blit(myfont_body.render("NEXT", 1, THECOLORS['antiquewhite']), (730,538))
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (610, 525, 100, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (615, 530, 90, 50))
    screen.blit(myfont_body.render("BACK", 1, THECOLORS['antiquewhite']), (620,538))

#Procedure to display main menu button--------------------
def main_menu_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (325, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (330, 500, 170, 50))
    screen.blit(myfont_body.render("Main Menu", 1, THECOLORS['antiquewhite']), (345,505))

#Procedure to display lesson button-----------------------
def lesson_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (525, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (530, 500, 170, 50))
    screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (565,505))

#Procedure to display restart button----------------------
def restart_button():
    pygame.draw.rect(screen, THECOLORS['antiquewhite'], (125, 495, 180, 60))
    pygame.draw.rect(screen, THECOLORS['brown'], (130, 500, 170, 50))
    screen.blit(myfont_body.render("Restart", 1, THECOLORS['antiquewhite']), (170,505))    

#Procedure to fade the screen to black--------------------
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


# The Game Loop------------------------------------------------------------------------------------------------------------------------------------------
running=True
show="title screen"
correct_answers = 0
quiz_completed = False
try:
    while running:
        clock.tick(60) #frame rate/second
        
        #Depending on which show is used, show a different screen and buttons
        if show == "title screen":
            #Title screen
            surface = pygame.image.load("images/bluebg.jpg")
            screen.blit(surface,(0,0))
            
            #Displaying title
            phrase(myfont_title, "POISONOUS", "brown", 175, 50)
            phrase(myfont_title, "PYRAMID", "brown", 245, 150)
            
            #Add our info
            button("brown", 315, 245, 190, 110)
            phrase(myfont_body, "Simone Ghosh", "antiquewhite", 320, 250)
            phrase(myfont_body, "Mona Jiang", "antiquewhite", 320, 275)
            phrase(myfont_body, "L. Keras", "antiquewhite", 320, 300)
            phrase(myfont_body, "ICS207", "antiquewhite", 320, 325) 
            
            pygame.display.flip() #flip all changes onto the display window
            time.sleep(2) #<-- Window will pause and than change 
            show="main menu"
            
        elif show == "main menu":
            #Main menu/background image        
            surface = pygame.image.load("images/pyramids.jpg")
            screen.blit(surface,(0,0))
            
            #Displaying titles 
            phrase(myfont_title, "POISONOUS", "brown", 175, 50)
            phrase(myfont_title, "PYRAMID", "brown", 245, 125)
            phrase(myfont_body, "main menu", "brown", 350, 200)
            
            #Button for instructions
            button("brown", 175, 300, 150, 50)
            phrase(myfont_body, "Instructions", "antiquewhite", 180, 305)
        
            #Button for lesson
            button("brown", 335, 300, 150, 50)
            phrase(myfont_body, "Lesson", "antiquewhite", 365, 305)
            
            #Button for review
            button("brown", 500, 300, 150, 50)
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            phrase(myfont_body, "Review", "antiquewhite", 530, 305)
            
            #Button for review
            button("brown", 250, 400, 150, 50)
            phrase(myfont_body, "Quiz", "antiquewhite", 290, 405)
        
            #Button for quiz
            button("brown", 420, 400, 150, 50)
            phrase(myfont_body, "Results", "antiquewhite", 455, 405)
        
        elif show == "instructions":
            # instructions background
            surface = pygame.image.load("images/instructions.png")
            screen.blit(surface,(0,0))
            #title
            title=myfont_title.render("INSTRUCTIONS", True, THECOLORS["antiquewhite"])
            screen.blit(title, (120,50))
            #display text
            x=75
            y=160
            with open("textFiles/instructions.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40 #line spacing
                    
            #return to main
            pygame.draw.rect(screen, THECOLORS['brown'], (350, 545, 150, 50))
            screen.blit(myfont_body.render("Return", 1, THECOLORS['antiquewhite']), (385, 550))
            
        elif show == "lesson":
            #first screen background
            lesson_screen = pygame.image.load("images/lesson_background.png")
            screen.blit(lesson_screen,(0,0))
            
            #title
            screen.blit(lesson_font_big.render("LESSON", 1, THECOLORS['antiquewhite']), (200,50))
            #background for text
            pygame.draw.rect(screen, THECOLORS['aquamarine4'], (40, 150, 770, 120))
           #display text
            x=45
            y=160
           
            with open("textFiles/lessonintro.txt") as word_file:
                for sentence in word_file:
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                    y+=40 #line spacing

            #start button------
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (475, 315, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (480, 320, 275, 100))   
            screen.blit(myfont_title.render("START", 1, THECOLORS['antiquewhite']), (485,332))
            #main menu--------------
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (100, 315, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (105, 320, 275, 100))   
            screen.blit(myfont_title.render("Main menu", 1, THECOLORS['antiquewhite']), (110,332))

            #UNIT BUTTONS (could not use procedure because of different coordinates)
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
            
            pygame.display.flip() #update screen
        

        elif show=="lesson 1":
            #load background
            surface = pygame.image.load("images/lesson_screen_1.png")
            screen.blit(surface,(0,0))
            #title
            screen.blit(lesson_font_big.render("1. Geography", 1, THECOLORS['antiquewhite']), (175,50))
            
            #display text
            x=50 #width
            y=160 #height
            with open("textFiles/lesson_1_quick_geography.txt") as word_file:   #import text
                for sentence in word_file:
                    y+=40 #spacing
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))


            next_button_back_button()
            pygame.display.flip() #update screen

        elif show=="lesson 2":  #same comments from lesson 1
             
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            
            screen.blit(myfont_title.render("2. Timeline ", 1, THECOLORS['antiquewhite']), (135,35))
            
            x=50 
            y=85
            with open("textFiles/Lesson_2_egyptian_rule.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()

        elif show=="lesson 3":  #same comments from lesson 1
        
            surface = pygame.image.load("images/lesson_screen_1.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_title.render("3.The Old Kingdom ", 1, THECOLORS['antiquewhite']), (150,50))
            #text
            x=50
            y=160
            with open("textFiles/lesson_3_the_old_kingdom.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()

        elif show=="lesson 4": #same comments from lesson 1
            surface = pygame.image.load("images/lesson_screen_2.png")
            screen.blit(surface,(0,0))
            screen.blit(myfont_special.render("4. The Middle Kingdom and", 1, THECOLORS['antiquewhite']), (50,50))
            screen.blit(myfont_special.render("The Arts", 1, THECOLORS['antiquewhite']), (90,100))
            
            x=50
            y=120
            with open("textFiles/lesson_4_the_middle_kingdom.txt") as word_file:
                for sentence in word_file:
                    y+=40
                    screen.blit(myfont_medium.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            next_button_back_button()
            pygame.display.flip()
            
        elif show=="lesson 5": # same comments from lesson 1
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
            # set background
            lesson_screen = pygame.image.load("images/lesson_background.png")
            screen.blit(lesson_screen,(0,0))

            screen.blit(lesson_font_big.render("END OF LESSON!", 1, THECOLORS['antiquewhite']), (10,50))
           
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
            screen.blit(myfont_title.render("Main menu", 1, THECOLORS['antiquewhite']), (500,155))

            #back to start
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (495, 295, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 275, 100))   
            screen.blit(myfont_special.render("Back to start", 1, THECOLORS['antiquewhite']), (515,325))
            
            #reivew
            pygame.draw.rect(screen, THECOLORS['antiquewhite'], (495, 440, 285, 110))
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 445, 275, 100))   
            screen.blit(myfont_title.render("Review", 1, THECOLORS['antiquewhite']), (515,450))            

        
            pygame.display.flip()           
        
        #Review---------------------------------------------------------------------------------------------------------------------
        elif show == "review":
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
            
            #Preparing boolian value for review
            ready = False
            path_taken = False
            screen_black = False            
            
        
        #Review question 1--------------------------------------------
        elif show == "review Q1":
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
        
        #Show answer to question 1---------------------------------
        elif show == "answered RQ1":
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
            #If user answered question 1 correctly, go to next question
            if ready:
                show = "hidden path"
            
            #If user answered wrong gave user chance to continue or review lesson
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
        
        #ALlow user to switch paths-----------------------------
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
        
        #Animation - show users position on map----------
        elif show == "map 1":
            surface = pygame.image.load("images/map.png")
            screen.blit(surface,(0,0))       
            marker = pygame.image.load("images/flag.png")
            
            #short cut
            if path_taken:
                x=124
                while x<468:
                    x+=1
                    screen.blit(marker,(x,35))
                    pygame.display.flip()
                    screen.blit(surface,(0,0)) 
            
            #Normal path
            else:
                x=124 #position dot
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
            show="review Q2"    
            pygame.display.flip()
        
        #Question 2
        elif show == "review Q2":
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
        
        #Show users position in map
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
        
        #Find the match
        elif show == "find match":
            surface = pygame.image.load("images/split path.png")
            screen.blit(surface,(0,0))
            
            #Make screen black
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
            
            #Timer
            text_rect = text.get_rect(center = window.get_rect().center)
            if counter<=10:
                window.blit(text, text_rect)
            
            match = pygame.image.load("images/match.png")
            screen.blit(match,(765,175)) 
         
            pygame.display.flip()
        
        #Show users position on map
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
            show="review Q3"    
            pygame.display.flip()
            
        #Question 3
        elif show == "review Q3":
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
        
        #Show users position on map 
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
            show="review Q4"    
            pygame.display.flip()
        
        #Question 4
        elif show == "review Q4":
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
        
        #Show users position on map
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
        
        #Alloq user to choose to drink, water, or eat
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
        
        #Show users position on map
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
            show="review Q5"    
            pygame.display.flip()
        
        #Question 5
        elif show == "review Q5":
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
        
        #Show users position on map
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
            #buttons
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
            #buttons
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
                    
            #buttons
            main_menu_button()
            lesson_button()
            restart_button()
            #update screen
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
            
            #button
            main_menu_button()
            lesson_button()
            restart_button()
            pygame.display.flip()
            
        elif show == "quiz":
            surface = pygame.image.load("images/egp_pyramidssphinx.jpg")
            screen.blit(surface,(0,0))
            
            #procedure
            phrase(myfont_title, "QUIZ", "brown", 315, 50)
            
            #Display a speech
            x=180
            y=135
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            with open("textFiles/start quiz.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    phrase(myfont_small, sentence, "antiquewhite", x, y)
            
            #Button to lesson
            button("brown", 175, 350, 150, 50)
            phrase(myfont_body, "Lesson", "antiquewhite", 205, 360)
            
            #Button for main menu
            button("brown", 335, 350, 150, 50)
            phrase(myfont_body, "Main menu", "antiquewhite", 340, 360)
            
            #Button to begin quiz
            button("brown", 500, 350, 150, 50)
            phrase(myfont_body, "Start", "antiquewhite", 545, 360)
            
        elif show=="answering Q1":
            question()
            score(correct_answers)

            phrase(myfont_body, "Who is the Egyptian god of the Nile?", "antiquewhite", 190, 180)
            phrase(myfont_body, "Hathor", "antiquewhite", 210, 305)
            phrase(myfont_body, "Hapi", "antiquewhite", 545, 305)
            phrase(myfont_body, "Horus", "antiquewhite", 215, 410)
            phrase(myfont_body, "Nile", "antiquewhite", 545, 410)

        elif show=="answered Q1":
            #Button for correct answer
            button("green", 500, 300, 150, 50)
            phrase(myfont_body, "Hapi", "black", 545, 305)
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q2"
            
        elif show=="answering Q2":
            question()
            score(correct_answers)
            
            phrase(myfont_body, "What land was known as the 'Kemet'?", "antiquewhite", 190, 180)
            phrase(myfont_small, "Nutrient filled river", "antiquewhite", 180, 302)
            phrase(myfont_small, "banks beside the Nile", "antiquewhite", 180, 317)
            phrase(myfont_small, "river", "antiquewhite", 180, 333)
            phrase(myfont_small, "Nutrient depleted river", "antiquewhite", 505, 302)
            phrase(myfont_small, "banks beside the", "antiquewhite", 505, 317)
            phrase(myfont_small, "Nile river", "antiquewhite", 505, 333)
            phrase(myfont_small, "There was no land", "antiquewhite", 190, 405)
            phrase(myfont_small, "known as 'Kemet'?", "antiquewhite", 190, 420)
            phrase(myfont_small, "Nutrient depleted river?", "antiquewhite", 505, 405)
            phrase(myfont_small, "banks.?", "antiquewhite", 505, 420)
                        
        elif show=="answered Q2":
            #Button for correct answer
            button("green", 175, 300, 150, 50)
            phrase(myfont_small, "Nutrient filled river", "black", 180, 302)
            phrase(myfont_small, "banks beside the Nile", "black", 180, 317)
            phrase(myfont_small, "river", "black", 180, 333)
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q3"
            
        elif show=="answering Q3":
            question()
            score(correct_answers) 
            
            phrase(myfont_body, "Where is upper Egypt located?", "antiquewhite", 230, 180)
            phrase(myfont_small, "The South of Egypt", "antiquewhite", 190, 315)
            phrase(myfont_small, "The North of Egypt", "antiquewhite", 515, 315)
            phrase(myfont_small, "The West of Egypt", "antiquewhite", 190, 415)
            phrase(myfont_small, "The East of Egypt", "antiquewhite", 515, 415)
                        
        elif show=="answered Q3":
            #Button for correct answer
            button("green", 175, 300, 150, 50)
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            phrase(myfont_small, "The South of Egypt", "black", 190, 315)
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q4" 
            
        elif show=="answering Q4":
            question()
            score(correct_answers)
            
            phrase(myfont_body, "What is a Dynasty?", "antiquewhite", 300, 180)
            phrase(myfont_small, "That is not a word.", "antiquewhite", 195, 315)
            phrase(myfont_small, "A family of peasents.", "antiquewhite", 510, 315)
            phrase(myfont_small, "A succession of rulers", "antiquewhite", 180, 405)
            phrase(myfont_small, "from different families.", "antiquewhite", 180, 420)
            phrase(myfont_small, "A succession of rulers", "antiquewhite", 505, 405)
            phrase(myfont_small, "from the same family,", "antiquewhite", 505, 420)
            
        elif show=="answered Q4":
            #Button for correct answer
            button("green", 500, 400, 150, 50)
            phrase(myfont_small, "A succession of rulers", "black", 505, 405)
            phrase(myfont_small, "from the same family,", "black", 505, 420)
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q5"
            
        elif show=="answering Q5":
            question()
            score(correct_answers)
            
            phrase(myfont_body, "What time period was the", "antiquewhite", 255, 155)
            phrase(myfont_body, "old kingdom?", "antiquewhite", 325, 200)
            phrase(myfont_small, "2800 BCE-2300 BCE.", "antiquewhite", 180, 315)
            phrase(myfont_small, "2700 BCE-2200 BCE.", "antiquewhite", 505, 315)
            phrase(myfont_small, "3800 BCE-3300 BCE.", "antiquewhite", 180, 415)
            phrase(myfont_small, "None of the above.", "antiquewhite", 515, 415)
            
        elif show=="answered Q5":
            #Button for correct answer
            button("green", 500, 300, 150, 50)
            phrase(myfont_small, "2700 BCE-2200 BCE.", "black", 505, 315)
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q6"
            
        elif show=="answering Q6":
            question()
            score(correct_answers)
            
            phrase(myfont_body, "How many great pyramids are there?", "antiquewhite", 190, 180)
            phrase(myfont_body, "2", "antiquewhite", 245, 305)
            phrase(myfont_body, "32", "antiquewhite", 560, 305)
            phrase(myfont_body, "60", "antiquewhite", 235, 410)
            phrase(myfont_body, "30", "antiquewhite", 560, 410)
            
        elif show=="answered Q6":
            #Button for correct answer
            button("green", 500, 400, 150, 50)
            screen.blit(myfont_body.render("30", 1, THECOLORS['black']), (560,410)) 
            
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q7"                        
            
        elif show=="answering Q7":    
            question()
            score(correct_answers)
            
            phrase(myfont_body, "Finish the sentence:", "antiquewhite", 300, 155)
            phrase(myfont_body, "The great sphinx is _______.", "antiquewhite", 245, 200)
            phrase(myfont_small, "Half man half lion", "antiquewhite", 190, 315)
            phrase(myfont_small, "Half man half cat", "antiquewhite", 520, 315)
            phrase(myfont_small, "half man half sphinx", "antiquewhite", 185, 415)
            phrase(myfont_small, "a human", "antiquewhite", 545, 415)
            
        elif show=="answered Q7":  
            #Button for correct answer
            button("green", 175, 300, 150, 50)
            phrase(myfont_small, "Half man half lion", "black", 190, 315)
        
            score(correct_answers)
            
            pygame.display.flip()
            time.sleep(3)
            show="complete" 
        
        elif show=="complete":
            screen.blit(surface,(0,0))
            quiz_completed = True
            
            #Displaying titles 
            phrase(myfont_title, "QUIZ", "brown", 315, 50)
            
            #Display a speech
            button("brown", 175, 150, 475, 150)
            x=180
            y=160
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            with open("textFiles/complete quiz.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    phrase(myfont_small, sentence, "antiquewhite", x, y)
            
            #Button to Main menu
            button("brown", 175, 350, 150, 50)
            phrase(myfont_body, "Main menu", "antiquewhite", 180, 360)
                    
            #Button to begin results
            button("brown", 500, 350, 150, 50)
            phrase(myfont_body, "Results", "antiquewhite", 520, 360)
            
        elif show=="results":
            #the surface here is the same as last time so the variable 'surface' already has an image stored
            screen.blit(surface,(0,0))
            
            phrase(myfont_title, "RESULTS", "brown", 225, 50)
            
            if quiz_completed: #percentage score
                result = round((correct_answers/7)*100, 2)
                if result%1==0:
                    result=int(result)   
                
                #Button to return to main menu
                button("brown", 325, 450, 175, 50)
                phrase(myfont_body, "Main menu", "antiquewhite", 345, 460)
            
                if result > 59: #pass
                    #Display a speech
                    button("brown", 175, 150, 475, 150)
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/pass quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            phrase(myfont_body, sentence, "antiquewhite", x, y)
                    phrase(myfont_body, "Score: "+str(correct_answers)+"/7", "antiquewhite", 180, 255)

                    #Display mark
                    button("green", 175, 350, 475, 50)
                    phrase(myfont_body, "Grade: "+str(result)+"%", "black", 345, 360)
                    
                else: #fail
                    #Display a speech
                    button("brown", 175, 150, 475, 150)
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/fail quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            phrase(myfont_body, sentence, "antiquewhite", x, y)
                    phrase(myfont_body, "Score: "+str(correct_answers)+"/7", "antiquewhite", 180, 255)
                
                    #Display mark
                    button("red", 175, 350, 475, 50)
                    phrase(myfont_body, "Grade: "+str(result)+"%", "antiquewhite", 342, 360)
            
            else:
                #Display a speech
                button("brown", 175, 150, 475, 150)
                x=180
                y=175
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                with open("textFiles/incomplete quiz.txt") as word_file:
                    for sentence in word_file:
                        y+=20
                        phrase(myfont_small, sentence, "antiquewhite", x, y)
                        
                #Button to lesson
                button("brown", 175, 350, 150, 50)
                phrase(myfont_body, "Main menu", "antiquewhite", 180, 360)
            
                #Button to begin quiz
                button("brown", 500, 350, 150, 50)
                phrase(myfont_body, "Quiz", "antiquewhite", 545, 360)               
                        
        
        # The Event Loop---------------------------------------------------------------------------------------------------------------------------------
        events=pygame.event.get()
            
        #Allow user to click buttons----------------------------------------------------------------------------------
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            
            #Main menu buttons----------------------------------------------------------------------------------------
            if show=="main menu":
                #Button for intructions 
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show = "instructions"
                
                #Button for lesson
                elif x>335 and x<335+150 and y>300 and y<300+50 and butt[0]==1:
                    show = "lesson"
                
                #Button for review
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show = "review"    
                
                #Button for quiz
                elif x>250 and x<250+150 and y>400 and y<400+50 and butt[0]==1:
                    show = "quiz"
                    
                #Button for results
                elif x>425 and x<425+150 and y>400 and y<400+50 and butt[0]==1:
                    show = "results"
            
            #Intructions----------------------------------------------------------------------------------------------
            elif show=="instructions":
                if x>350 and x<350+150 and y>545 and y<545+50 and butt[0]==1:
                    show = "main menu"    
            
            #Lesson---------------------------------------------------------------------------------------------------
            elif show == "lesson": #from lesson page
                #start button
                if x>475 and x<475+285 and y>315 and y<315+110 and butt[0]==1:
                    show = "lesson 1"
                #Main mneu button
                elif x>105 and x<105+285 and y>315 and y<315+110 and butt[0]==1:
                    show = "main menu"

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
                    
            #Final page
            elif show=="done":
                #go to main menu
                if x>495 and x<495+285 and y>150 and y<150+110 and butt[0]==1:
                    show = "main menu"
                
                #GO to lesson
                elif x>495 and x<495+285 and y>295 and y<295+110 and butt[0]==1:
                    show="lesson"
                
                #Go to review
                elif x>495 and x<495+285 and y>440 and y<440+110 and butt[0]==1:
                    show="review"
                    
            #Review buttons=------------------------------------------------------------------------------------------
            elif show=="review":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"                
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                    show="review Q1"
            
            #Question 1
            elif show=="review Q1": 
                if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                    show="answered RQ1"
                    ready=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="answered RQ1"    
            
            #Answers to Question 1
            elif show=="prepared":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"                
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                    show="hidden path"                
            
            #Ask user if they want to take a short cut
            elif show=="hidden path":
                if x>175 and x<175+475 and y>300 and y<300+50 and butt[0]==1:
                    show="map 1"
                    path_taken=True
                elif x>175 and x<175+475 and y>400 and y<400+50 and butt[0]==1:
                    show="map 1"                 
            
            #Question 2
            elif show=="review Q2":
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
            
            #User finds a match or dies
            elif show=="find match":
                if x>765 and x<765+24 and y>175 and y<175+24 and butt[0]==1: #<-- match
                    show="map 3"
                elif event.type == timer_event: #<-- timer 
                    counter -= 1
                    text = myfont_title.render(str(counter), True, (THECOLORS["antiquewhite"]))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)  
                        show="ending 2"                
            
            #Question 3
            elif show=="review Q3":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="map 4"          
            
            #Question 4
            elif show=="review Q4":
                if x>175 and x<175+200 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>450 and x<450+200 and y>300 and y<300+50 and butt[0]==1:
                    show="map 5"     
                elif x>175 and x<175+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"
                elif x>450 and x<450+200 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"                     
            
            #User chooses to drink, eat, or sleep. And if they decide to drink they continue, else they die
            elif show=="drink eat sleep":
                if x>175 and x<175+475 and y>250 and y<250+50 and butt[0]==1:
                    show="map 6"
                elif x>175 and x<175+475 and y>350 and y<350+50 and butt[0]==1:
                    show="ending 3b"
                elif x>175 and x<175+475 and y>450 and y<450+50 and butt[0]==1:
                    show="ending 3a"
                    
            #Question 5
            elif show=="review Q5":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="ending 1"     
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="map 7"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="ending 1"     
            
            #Endings (deaths) 
            #these endings all have the same button coordinates
            elif show=="ending 1" or show=="ending 2" or show=="ending 3a" or show=="ending 3b" or show=="ending 4":
                #Main menu
                if x>330 and x<330+170 and y>500 and y<500+50 and butt[0]==1:
                    show="main menu"
                #Lesson
                elif x>530 and x<530+170 and y>500 and y<500+50 and butt[0]==1:
                    show="lesson"
                #Review
                elif x>130 and x<130+170 and y>500 and y<500+50 and butt[0]==1:
                    show="review"
                    
            #Quiz-----------------------------------------------------------------------------------------------------
            elif show=="quiz":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1: #<-- go to lesson
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1: #<-- go to main menu
                    show="main menu"                
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1: #<-- start quiz
                    show="answering Q1"
            
            #Question 1
            elif show=="answering Q1":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q1"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q1"
                    correct_answers += 1 
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q1"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q1"         
            
            #Question 2
            elif show=="answering Q2":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    correct_answers += 1 #increase score (add into accumulator)
                    show="answered Q2"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q2"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q2"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q2"      
            
            #Question 3
            elif show=="answering Q3":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    correct_answers += 1
                    show="answered Q3"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q3"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q3"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q3"    
            
            #Question 4
            elif show=="answering Q4":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q4"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q4"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q4"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    correct_answers += 1
                    show="answered Q4"     
           
            #Question 5
            elif show=="answering Q5":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q5"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    correct_answers += 1
                    show="answered Q5"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q5"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q5"    
            
            #Quesiton 6
            elif show=="answering Q6":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q6"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q6"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q6"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    correct_answers += 1
                    show="answered Q6"  
           
            #Question 7
            elif show=="answering Q7":
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1:
                    correct_answers += 1
                    show="answered Q7"
                elif x>500 and x<500+150 and y>300 and y<300+50 and butt[0]==1:
                    show="answered Q7"
                elif x>175 and x<175+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q7"
                elif x>500 and x<500+150 and y>400 and y<400+50 and butt[0]==1:
                    show="answered Q7"           
            
            #View results or return to main menu
            elif show=="complete":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                    show="results"            
            
            #Results--------------------------------------------------------------------------------------------------
            if show=="results":
                #If the quiz is completed
                if quiz_completed:
                    if x>325 and x<325+175 and y>450 and y<450+50 and butt[0]==1: #<-- main menu button
                        show="main menu"      
                
                #If user has not completed quiz
                else:
                    if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1: #<-- main menu button
                        show="main menu"
                    elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1: #<-- start quiz button
                        show="quiz"  
            #return to main menu
            if event.type==KEYDOWN and event.key==K_RETURN: 
                show="main menu"
            #Exit/credits-----------------------------------------------------------------------------------------------------    
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
        
# Event Handling End #-----------------------------------------------------------------------------------------------------------------------------------
finally:
    pygame.quit()  # Keep this IDLE friendly
