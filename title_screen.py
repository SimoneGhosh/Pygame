import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("To be named later")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)