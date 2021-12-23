import pygame
import THECOLORS
from sys import exit

pygame.init()
screen = pygame.display.set_mode((850,600))
pygame.display.set_caption("Poisonous Pyramid")
clock = pygame.time.Clock()
colour = (196,90,64)
screen.fill(colour)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)

font = pygame.font.sysfont(None,25)
def message_to_screen(msg, color):
    screeen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [425, 300])
message_to_screen("Welcome to Poisonous Pyramid!", yellow)
