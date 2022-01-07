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
            
            #Displaying titles 
            title=myfont_title.render("QUIZ", True, THECOLORS["brown"])
            screen.blit(title, (315,50))
            
            #Display a speech
            x=180
            y=135
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            with open("textFiles/starting quiz.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_small.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            
            #Button to lesson
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
            screen.blit(myfont_body.render("Lesson", 1, THECOLORS['antiquewhite']), (205,360)) 
            
            #Button for main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (335, 350, 150, 50))
            screen.blit(myfont_body.render("Main menu", 1, THECOLORS['antiquewhite']), (340,355))
            
            #Button to begin quiz
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
            screen.blit(myfont_body.render("Start", 1, THECOLORS['antiquewhite']), (545,360))   
            
        elif show=="answering Q1":
            screen.blit(surface,(0,0))
            
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Who is the Egyptian god of the Nile?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Hathor", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Hapi", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("Horus", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("Nile", 1, THECOLORS['antiquewhite']), (545,410))        
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            pygame.display.flip()
            
        elif show=="answered Q1":
            screen.blit(surface,(0,0))
            
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Who is the Egyptian god of the Nile?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Hathor", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Hapi", 1, THECOLORS['black']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("Horus", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("Nile", 1, THECOLORS['antiquewhite']), (545,410))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q2"
            
        elif show=="answering Q2":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What land was known as the 'Kemet'?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("Nutrient filled river", 1, THECOLORS['antiquewhite']), (180,302))
            screen.blit(myfont_small.render("banks beside the Nile", 1, THECOLORS['antiquewhite']), (180,317))
            screen.blit(myfont_small.render("river.", 1, THECOLORS['antiquewhite']), (180,333))
         
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("Nutrient depleted river", 1, THECOLORS['antiquewhite']), (505,302))
            screen.blit(myfont_small.render("banks beside the", 1, THECOLORS['antiquewhite']), (505,317))
            screen.blit(myfont_small.render("Nile river.", 1, THECOLORS['antiquewhite']), (505,333))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("There was no land", 1, THECOLORS['antiquewhite']), (190,405)) 
            screen.blit(myfont_small.render("known as 'kemet'.", 1, THECOLORS['antiquewhite']), (190,420)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("Nutrient depleted river", 1, THECOLORS['antiquewhite']), (505,405))   
            screen.blit(myfont_small.render("banks.", 1, THECOLORS['antiquewhite']), (505,420))   
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))          
            pygame.display.flip()
            
        elif show=="answered Q2":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What land was known as the 'Kemet'?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("Nutrient filled river", 1, THECOLORS['black']), (180,302))
            screen.blit(myfont_small.render("banks beside the Nile", 1, THECOLORS['black']), (180,317))
            screen.blit(myfont_small.render("river.", 1, THECOLORS['black']), (180,333))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("Nutrient depleted river", 1, THECOLORS['antiquewhite']), (505,302))
            screen.blit(myfont_small.render("banks beside the", 1, THECOLORS['antiquewhite']), (505,317))
            screen.blit(myfont_small.render("Nile river.", 1, THECOLORS['antiquewhite']), (505,333))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("There was no land", 1, THECOLORS['antiquewhite']), (190,405)) 
            screen.blit(myfont_small.render("known as 'kemet'.", 1, THECOLORS['antiquewhite']), (190,420))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("Nutrient depleted river", 1, THECOLORS['antiquewhite']), (505,405))   
            screen.blit(myfont_small.render("banks.", 1, THECOLORS['antiquewhite']), (505,420)) 
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q3"
            
        elif show=="answering Q3":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Where is upper Egypt located?", 1, THECOLORS['antiquewhite']), (230,180))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("The South of Egypt", 1, THECOLORS['antiquewhite']), (190,315))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("The North of Egypt", 1, THECOLORS['antiquewhite']), (515,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("The West of Egypt", 1, THECOLORS['antiquewhite']), (190,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("The East of Egypt", 1, THECOLORS['antiquewhite']), (515,415))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            pygame.display.flip()                 
            
        elif show=="answered Q3":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Where is upper Egypt located?", 1, THECOLORS['antiquewhite']), (230,180))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("The South of Egypt", 1, THECOLORS['black']), (190,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("The North of Egypt", 1, THECOLORS['antiquewhite']), (515,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("The West of Egypt", 1, THECOLORS['antiquewhite']), (190,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("The East of Egypt", 1, THECOLORS['antiquewhite']), (515,415))      
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q4" 
            
        elif show=="answering Q4":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What is a Dynasty?", 1, THECOLORS['antiquewhite']), (300,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("That is not a word.", 1, THECOLORS['antiquewhite']), (195,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("A family of peasents.", 1, THECOLORS['antiquewhite']), (510,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("A succession of rulers", 1, THECOLORS['antiquewhite']), (180,405)) 
            screen.blit(myfont_small.render("from different families.", 1, THECOLORS['antiquewhite']), (180,420)) 
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("A succession of rulers", 1, THECOLORS['antiquewhite']), (505,405))
            screen.blit(myfont_small.render("from the same family.", 1, THECOLORS['antiquewhite']), (505,420))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            
        elif show=="answered Q4":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What is a Dynasty?", 1, THECOLORS['antiquewhite']), (300,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("That is not a word.", 1, THECOLORS['antiquewhite']), (195,315))

            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("A family of peasents.", 1, THECOLORS['antiquewhite']), (510,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("A succession of rulers", 1, THECOLORS['antiquewhite']), (180,405)) 
            screen.blit(myfont_small.render("from different families.", 1, THECOLORS['antiquewhite']), (180,420)) 
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("A succession of rulers", 1, THECOLORS['black']), (505,405))
            screen.blit(myfont_small.render("from the same family.", 1, THECOLORS['black']), (505,420))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q5"
            
        elif show=="answering Q5":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What time period was the", 1, THECOLORS['antiquewhite']), (255,155))
            screen.blit(myfont_body.render("old kingdom?", 1, THECOLORS['antiquewhite']), (325,200))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("2800 BCE-2300 BCE.", 1, THECOLORS['antiquewhite']), (180,315))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("2700 BCE-2200 BCE.", 1, THECOLORS['antiquewhite']), (505,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("3800 BCE-3300 BCE.", 1, THECOLORS['antiquewhite']), (180,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("None of the above.", 1, THECOLORS['antiquewhite']), (515,415))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105)) 
            pygame.display.flip()
            
        elif show=="answered Q5":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What time period was the", 1, THECOLORS['antiquewhite']), (255,155))
            screen.blit(myfont_body.render("old kingdom?", 1, THECOLORS['antiquewhite']), (325,200))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("2800 BCE-2300 BCE.", 1, THECOLORS['antiquewhite']), (180,315))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("2700 BCE-2200 BCE.", 1, THECOLORS['black']), (505,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("3800 BCE-3300 BCE.", 1, THECOLORS['antiquewhite']), (180,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("None of the above.", 1, THECOLORS['antiquewhite']), (515,415))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q6"
            
        elif show=="answering Q6":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("How many great pyramids are there?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2", 1, THECOLORS['antiquewhite']), (245,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("32", 1, THECOLORS['antiquewhite']), (560,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("60", 1, THECOLORS['antiquewhite']), (235,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("30", 1, THECOLORS['antiquewhite']), (560,410))  
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))        
            pygame.display.flip()
            
        elif show=="answered Q6":
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("How many great pyramids are there?", 1, THECOLORS['antiquewhite']), (190,180))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2", 1, THECOLORS['antiquewhite']), (245,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("32", 1, THECOLORS['antiquewhite']), (560,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("60", 1, THECOLORS['antiquewhite']), (235,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("30", 1, THECOLORS['black']), (560,410)) 
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="answering Q7"                        
            
        elif show=="answering Q7":    
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("finish the sentence:", 1, THECOLORS['antiquewhite']), (300,155))
            screen.blit(myfont_body.render("The great sphinx is _______.", 1, THECOLORS['antiquewhite']), (245,200))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("Half man half lion", 1, THECOLORS['antiquewhite']), (190,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("Half man half cat", 1, THECOLORS['antiquewhite']), (520,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("half man half sphinx", 1, THECOLORS['antiquewhite']), (185,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("a human", 1, THECOLORS['antiquewhite']), (545,415))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))          
            pygame.display.flip()
            
        elif show=="answered Q7":  
            screen.blit(surface,(0,0))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("finish the sentence:", 1, THECOLORS['antiquewhite']), (300,155))
            screen.blit(myfont_body.render("The great sphinx is _______.", 1, THECOLORS['antiquewhite']), (245,200))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_small.render("Half man half lion", 1, THECOLORS['black']), (190,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_small.render("Half man half cat", 1, THECOLORS['antiquewhite']), (520,315))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_small.render("half man half sphinx", 1, THECOLORS['antiquewhite']), (185,415)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_small.render("a human", 1, THECOLORS['antiquewhite']), (545,415))
            
            pygame.draw.rect(screen, THECOLORS['brown'], (330, 95, 150, 50))
            screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (345,105))
            
            pygame.display.flip()
            time.sleep(3)
            show="complete" 
        
        elif show=="complete":
            screen.blit(surface,(0,0))
            quiz_completed = True
            
            #Displaying titles 
            title=myfont_title.render("QUIZ", True, THECOLORS["brown"])
            screen.blit(title, (315,50))
            
            #Display a speech
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            x=180
            y=160
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
            with open("textFiles/quiz complete.txt") as word_file:
                for sentence in word_file:
                    y+=20
                    screen.blit(myfont_small.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
            
            #Button to Main menu
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
            screen.blit(myfont_body.render("Main menu", 1, THECOLORS['antiquewhite']), (180,360)) 
        
            #Button to begin results
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
            screen.blit(myfont_body.render("Results", 1, THECOLORS['antiquewhite']), (520,360)) 
            
        elif show=="results":
            screen.blit(surface,(0,0))
            
            title=myfont_title.render("RESULTS", True, THECOLORS["brown"])
            screen.blit(title, (225,50))            
            
            if quiz_completed:
                result = round((correct_answers/7)*100, 2)
                if result%1==0:
                    result=int(result)   
                
                #Button to return to main menu
                pygame.draw.rect(screen, THECOLORS['brown'], (325, 450, 175, 50))
                screen.blit(myfont_body.render("Main menu", 1, THECOLORS['antiquewhite']), (345,460))    
            
                if result > 59:
                    #Display a speech
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/pass quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))                    
                    screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (180,255))

                    #Display mark
                    pygame.draw.rect(screen, THECOLORS['green'], (175, 350, 475, 50))
                    screen.blit(myfont_body.render("Grade: "+str(result)+"%", 1, THECOLORS['black']), (345,360))                
                else:
                    #Display a speech
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    x=180
                    y=105
                    pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                    with open("textFiles/fail quiz.txt") as word_file:
                        for sentence in word_file:
                            y+=50
                            screen.blit(myfont_body.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))                     
                    screen.blit(myfont_body.render("Score: "+str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (180,255))
                
                    #Display mark
                    pygame.draw.rect(screen, THECOLORS['red'], (175, 350, 475, 50))
                    screen.blit(myfont_body.render("Grade: "+str(result)+"%", 1, THECOLORS['antiquewhite']), (342,360))  
            
            else:
                #Display a speech
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                x=180
                y=175
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 150))
                with open("textFiles/incomplete quiz.txt") as word_file:
                    for sentence in word_file:
                        y+=20
                        screen.blit(myfont_small.render(sentence, 1, THECOLORS['antiquewhite']), (x,y))
                        
                #Button to lesson
                pygame.draw.rect(screen, THECOLORS['brown'], (175, 350, 150, 50))
                screen.blit(myfont_body.render("Main Menu", 1, THECOLORS['antiquewhite']), (180,360)) 
            
                #Button to begin quiz
                pygame.draw.rect(screen, THECOLORS['brown'], (500, 350, 150, 50))
                screen.blit(myfont_body.render("Quiz", 1, THECOLORS['antiquewhite']), (545,360))                
                        
        
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