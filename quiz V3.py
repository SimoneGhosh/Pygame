"""
Author: Simone
Date: 2022-01-09
Name: quiz
Description: adjusted quiz by using procedures
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

def question():
    screen.blit(surface,(0,0))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
    pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
    
def phrase(font, answer, colour, width, length):
    screen.blit(font.render(answer, 1, THECOLORS[colour]), (width,length))
        
def score(correct_answers):
    pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
    screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
    
# The Game Loop
running=True
show="quiz"
correct_answers = 0
graded = False

try:
    while running:
        clock.tick(60)
        
        if show == "quiz":
            correct_answers = 0
            surface = pygame.image.load("images/egp_pyramidssphinx.jpg")
            screen.blit(surface,(0,0))
            
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
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
            phrase(myfont_body, "Lesson", "antiquewhite", 205, 360)
            
            #Button for main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (335, 350, 150, 50))
            phrase(myfont_body, "Main menu", "antiquewhite", 340, 360)
            
            #Button to begin quiz
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
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
            phrase(myfont_small, "3800 BCE-3300 BCE.", "antiquewhite", 180, 405)
            phrase(myfont_small, "None of the above.", "antiquewhite", 515, 405)
            
        elif show=="answered Q5":
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
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
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            x=180
            y=160
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            with open("textFiles/complete quiz.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    phrase(myfont_small, sentence, "antiquewhite", x, y)
            
            #Button to Main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
            phrase(myfont_body, "Main menu", "antiquewhite", 180, 360)
                    
            #Button to begin results
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
            phrase(myfont_body, "Results", "antiquewhite", 520, 360)
            
        elif show=="results":
            screen.blit(surface,(0,0))
            
            phrase(myfont_title, "RESULTS", "brown", 225, 50)
            
            if quiz_completed:
                result = round((correct_answers/7)*100, 2)
                if result%1==0:
                    result=int(result)   
                
                #Button to return to main menu
                pygame.draw.rect(screen, THECOLORS['brown'], (325, 450, 175, 50))
                phrase(myfont_body, "Main menu", "antiquewhite", 345, 460)
            
                if result > 59:
                    #Display a speech
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/pass quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            phrase(myfont_body, sentence, "antiquewhite", x, y)
                    phrase(myfont_body, "Score: "+str(correct_answers)+"/7", "antiquewhite", 180, 255)

                    #Display mark
                    pygame.draw.rect(screen, THECOLORS['green'], (175, 350, 475, 50))
                    phrase(myfont_body, "Grade: "+str(result)+"%", "black", 345, 360)
                else:
                    #Display a speech
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/fail quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            phrase(myfont_body, sentence, "antiquewhite", x, y)
                    phrase(myfont_body, "Score: "+str(correct_answers)+"/7", "antiquewhite", 180, 255)
                
                    #Display mark
                    pygame.draw.rect(screen, THECOLORS['red'], (175, 350, 475, 50))
                    phrase(myfont_body, "Grade: "+str(result)+"%", "antiquewhite", 342, 360)
            
            else:
                #Display a speech
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                x=180
                y=175
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                with open("textFiles/incomplete quiz.txt") as word_file:
                    for sentence in word_file:
                        y+=20
                        phrase(myfont_small, sentence, "antiquewhite", x, y)
                        
                #Button to lesson
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
                phrase(myfont_body, "Main menu", "antiquewhite", 180, 360)
            
                #Button to begin quiz
                pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
                phrase(myfont_body, "Quiz", "antiquewhite", 545, 360)                        
        
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
            if show=="quiz":
                if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                    show="lesson"
                elif x>335 and x<335+150 and y>350 and y<350+50 and butt[0]==1:
                    show="main menu"   
                elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
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
                    correct_answers += 1
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
            
            #Results
            if show=="results":
                if quiz_completed:
                    if x>325 and x<325+175 and y>450 and y<450+50 and butt[0]==1:
                        show="main menu"      
                else:
                    if x>175 and x<175+150 and y>350 and y<350+50 and butt[0]==1:
                        show="main menu"
                    elif x>500 and x<500+150 and y>350 and y<350+50 and butt[0]==1:
                        show="quiz"      
            
            #Allowing user to quit program    
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                running = False        
            
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly