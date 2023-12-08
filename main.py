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
    velocity = 0
    R = 46
    G = 21
    B = 71
#---------------------------------

Car = car()

camera_offset = [0,0]

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

    keys = pygame.key.get_pressed()

    x = 0
    y = 0
    a = 0
    b = 0

    if keys[pygame.K_RIGHT] == True:
        x = 1
    if keys[pygame.K_LEFT] == True:
        y = 1
    if keys[pygame.K_DOWN] == True:
        a = 1()
    if keys[pygame.K_UP] == True:
        b = 1
    Car.pos[0] = Car.pos[0] + ((x - y) * Car.velocity)
    Car.pos[1] += (a - b) * Car.velocity

    camera_offset[0] = Car.pos[0] - width / 2
    camera_offset[1] = Car.pos[1] - height / 2

    pygame.draw.rect(screen, (Car.R, Car.G, Car.B), ([ Car.pos[0] - camera_offset[0], Car.pos[1] - camera_offset[1] ], [ Car.size[0] , Car.size[1] ]))
    
    pygame.display.flip()