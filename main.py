import pygame
import random
import math
from sys import exit

height = 1900
width = 1030

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("The Drift")

clock = pygame.time.Clock()

framerate = 150

#---------------------------------
class car:
    pos = [300, 300]
    size = [215, 90]
    velocity = [0, 0]
    R = 46
    G = 21
    B = 71
#---------------------------------

Car = car()

#Update()
while 1:
    #count the time frame took and assign it to ms
    ms = clock.tick(framerate)

    #resets screen
    screen.fill((100, 100, 100))

    
    #detect events including inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.rect(screen, (Car.R, Car.G, Car.B), (Car.pos, Car.size))
    
    pygame.display.flip()