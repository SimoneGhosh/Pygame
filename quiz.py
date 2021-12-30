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

#Display background image
surface = pygame.image.load("images\pyramids.jpg")
screen.blit(surface,(0,0))

#Clock
clock = pygame.time.Clock()
refresh_rate=30

#Setting up the font and the size 
myfont_title = pygame.font.SysFont("Papyrus", 60)
myfont_body = pygame.font.SysFont("times new roman", 30)
test=pygame.display.get_driver()

# The Game Loop
running=True
show="answering Q1"

try:
    while running:
        clock.tick(60)
        
        if show=="answering Q1":
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Who is the Egyptian god of the Nile?", 1, THECOLORS['antiquewhite']), (210,175))
            
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
        
        elif show=="answered Q1":
            #Question
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Who is the Egyptian god of the Nile?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Hathor", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Hapi", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("Horus", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("Nile", 1, THECOLORS['antiquewhite']), (545,410))
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))
    
        elif show=="answering Q2":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What land was known as the 'Kemet'?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Nutrient filled river banks beside the Nile river.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Nutrient depleted river banks beside the Nile river.", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("There was no land known as 'kemet'.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("Nutrient depleted river banks beside the Blue Nile.", 1, THECOLORS['antiquewhite']), (545,410))   
        
        elif show=="answered Q2":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What land was known as the 'Kemet'?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Nutrient filled river banks beside the Nile river.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Nutrient depleted river banks beside the Nile river.", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("There was no land known as 'kemet'.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("Nutrient depleted river banks beside the Blue Nile.", 1, THECOLORS['antiquewhite']), (545,410))     
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))            
            
        elif show=="answering Q3":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Where is upper Egypt located?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("The South of Egypt", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("The North of Egypt", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("The West of Egypt", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("The North-West of Egypt", 1, THECOLORS['antiquewhite']), (545,410))
        
        elif show=="answered Q3":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("Where is upper Egypt located?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("The South of Egypt", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("The North of Egypt", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("The West of Egypt", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("The North-West of Egypt", 1, THECOLORS['antiquewhite']), (545,410))      
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))             
            
        elif show=="answering Q4":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What is a Dynasty?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("That is not a word.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("A family of peasents.", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("A succession of rulers from different families.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("A succession of rulers from the same family.", 1, THECOLORS['antiquewhite']), (545,410))
        
        elif show=="answered Q4":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What is a Dynasty?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("That is not a word.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("A family of peasents.", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("A succession of rulers from different families.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("A succession of rulers from the same family.", 1, THECOLORS['antiquewhite']), (545,410))
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))            
            
        elif show=="answering Q5":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What time period was the old kingdom?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2800 BCE-2300 BCE.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("2700 BCE-2200 BCE", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("3800 BCE-3300 BCE.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("There was no old kingdom.", 1, THECOLORS['antiquewhite']), (545,410))
        
        elif show=="answered Q5":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("What time period was the old kingdom?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2800 BCE-2300 BCE.", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("2700 BCE-2200 BCE", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("3800 BCE-3300 BCE.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("There was no old kingdom.", 1, THECOLORS['antiquewhite']), (545,410))      
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))              
            
        elif show=="answering Q6":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("How many great pyramids are there?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("32", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("60.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("30", 1, THECOLORS['antiquewhite']), (545,410))  
        
        elif show=="answered Q6":
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("How many great pyramids are there?", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("2", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("32", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("60.", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("30", 1, THECOLORS['antiquewhite']), (545,410)) 
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))             
            
        elif show=="answering Q7":            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("finish the sentence: The great sphinx is _______.", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Half man half lion", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Half man half cat", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("half man half sphinx", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['brown'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("a human", 1, THECOLORS['antiquewhite']), (545,410))
        
        elif show=="answered Q7":            
            pygame.draw.rect(screen, THECOLORS['brown'], (175, 150, 475, 100))
            screen.blit(myfont_body.render("finish the sentence: The great sphinx is _______.", 1, THECOLORS['antiquewhite']), (210,175))
            
            #Button for correct answer
            pygame.draw.rect(screen, THECOLORS['green'], (175, 300, 150, 50))
            screen.blit(myfont_body.render("Half man half lion", 1, THECOLORS['antiquewhite']), (210,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 300, 150, 50))
            screen.blit(myfont_body.render("Half man half cat", 1, THECOLORS['antiquewhite']), (545,305))
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (175, 400, 150, 50))
            screen.blit(myfont_body.render("half man half sphinx", 1, THECOLORS['antiquewhite']), (215,410)) 
        
            #Button for answer
            pygame.draw.rect(screen, THECOLORS['red'], (500, 400, 150, 50))
            screen.blit(myfont_body.render("a human", 1, THECOLORS['antiquewhite']), (545,410))  
            
            #Button to next question
            pygame.draw.rect(screen, THECOLORS['brown'], (695, 545, 150, 50))
            screen.blit(myfont_body.render("Next", 1, THECOLORS['antiquewhite']), (732,555))   
        
        elif show=="results":
            screen.blit(myfont_title.render(str(correct_answers)+"/7", 1, THECOLORS['antiquewhite']), (732,555))
        
        # The Event Loop #
        events=pygame.event.get()
            
        #Allow user to exit the game
        for event in events:       
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            correct_answers = int(0)
            
            # Detecting the click inside the button area
            #question 1
            if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q1":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q1":
                correct_answers += 1
                show=="answered Q1"
            elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q1":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q1":
                show=="answered Q1"
            
            elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q1":
                show=="answering Q2"            
                    
            #question 2:
            if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q2":
                correct_answers += 1
                show=="answered Q1"
            elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q2":
                show=="answered Q1"
            elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q2":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q2":
                show=="answered Q1"  
            
            elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q2":
                show=="answering Q3"            
                    
            #question 3:
            if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q3":
                correct_answers += 1
                show=="answered Q1"
            elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q3":
                show=="answered Q1"
            elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q3":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q3":
                show=="answered Q1"      
            
            elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q3":
                show=="answering Q4"            
                    
            #question 4:
            if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answeing Q4":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answeing Q4":
                show=="answered Q1"
            elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answeing Q4":
                show=="answered Q1"
            elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answeing Q4":
                correct_answers += 1
                show=="answered Q1"     
            
            elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q4":
                show=="answering Q5"             
                    
            #question 5:
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q5":
                    show=="answered Q1"
                elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q5":
                    correct_answers += 1
                    show=="answered Q1"
                elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q5":
                    show=="answered Q1"
                elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q5":
                    show=="answered Q1"     
                
                elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q5":
                    show=="answering Q6"                 
                    
            #quesiton 6:
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q6":
                    show=="answered Q1"
                elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q6":
                    show=="answered Q1"
                elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q6":
                    correct_answers += 1
                    show=="answered Q1"
                elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q6":
                    show=="answered Q1"  
                
                elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q6":
                    show=="answering Q7"                 
                    
            #question 7:
                if x>175 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q7":
                    correct_answers += 1
                    show=="answered Q7"
                elif x>500 and x<175+150 and y>300 and y<300+50 and butt[0]==1 and show=="answering Q7":
                    show=="answered Q7"
                elif x>175 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q7":
                    show=="answered Q7"
                elif x>500 and x<175+150 and y>400 and y<300+50 and butt[0]==1 and show=="answering Q7":
                    show=="answered Q7"           
                
                elif x>695 and x<695+150 and y>545 and y<545+50 and butt[0]==1 and show=="answered Q7":
                    show=="results"                 
                
            if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                running = False        
        
        pygame.display.update() 
        
# Event Handling End #
finally:
    pygame.quit()  # Keep this IDLE friendly