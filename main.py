import pygame
import random
import math
from sys import exit

height = 640
width = 480

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
    velocity = 5
    R = 46
    G = 21
    B = 71
#---------------------------------

Car = car()

#Update()
while 1:
    #count the time frame took and assign it to ms
    ms = clock.tick(framerate)
    screen.fill((100, 100, 100))

    #detect events including inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    Car.pos[0] += ((keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * Car.velocity)
    Car.pos[1] += ((keys[pygame.K_UP] - keys[pygame.K_DOWN]) * Car.velocity)

    pygame.draw.rect(screen, (255,255,255), 
                    ([ 200 - Car.pos[0], 200 - Car.pos[1]], 
                    [ Car.size[0] , Car.size[1]]))
    
    pygame.draw.rect(screen, (255,255,255), 
                ([ 100 - Car.pos[0], 100 - Car.pos[1]], 
                [ Car.size[0] , Car.size[1]]))
    
    pygame.draw.rect(screen, (255,255,255), 
                ([ 150 - Car.pos[0], 150 - Car.pos[1]], 
                [ Car.size[0] , Car.size[1]]))
    
    pygame.draw.rect(screen, (255,255,255), 
                ([ 300 - Car.pos[0], 300 - Car.pos[1]], 
                [ Car.size[0] , Car.size[1]]))

    pygame.draw.rect(screen, (Car.R, Car.G, Car.B), 
                     ([ (height / 2)- Car.size[0] / 2 , (width / 2)- Car.size[1] / 2], 
                      [ Car.size[0] , Car.size[1]]))

    pygame.display.flip()