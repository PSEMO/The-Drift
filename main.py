import pygame
import random
import math
import numpy as np
from sys import exit

height = 800
width = 600

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("The Drift")

clock = pygame.time.Clock()

framerate = 30

#---------------------------------
class car:
    pos = [300, 300]
    size = [54, 22]
    CurrentVelocity = 0
    MaxVelocity = 2.5
    MovingDegree = 0
    Degree = 0
    #Constant variables
    MaxRotation = 1
    Acceleration = 0.0001
    Drag = 0.00005
    R = 46
    G = 21
    B = 71
#---------------------------------
def degree_to_position (degree):
  # Convert degree to radian
  radian = degree * math.pi / 180
  # Calculate x and y coordinates
  x = math.cos (radian)
  y = math.sin (radian)
  # Return coordinates as a tuple
  return (x, y)
#---------------------------------
def draw_rectangle(x, y, width, height, color, rotation=0):
    """Draw a rectangle, centered at x, y.
    Arguments:
      x (int/float):
        The x coordinate of the center of the shape.
      y (int/float):
        The y coordinate of the center of the shape.
      width (int/float):
        The width of the rectangle.
      height (int/float):
        The height of the rectangle.
      color (str):
        Name of the fill color, in HTML format.
    """
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = -math.radians(rotation)

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(screen, color, points)
#---------------------------------
def Similarity(n1, n2):
    """ calculates a similarity score between 2 numbers """
    if n1 + n2 == 0:
        return 1
    else:
        return 1 - abs(n1 - n2) / (n1 + n2)
#---------------------------------

Car = car()
asd = 0

#Update()
while 1:

    #count the time frame took and assign it to ms
    ms = clock.tick(framerate)
    deltaTime = ms * 10
    #------------

    #resets screen
    screen.fill((100, 100, 100))
    #------------

    #detect events including inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #------------

    # get the user input
    keys = pygame.key.get_pressed()
    #------------

    #apply car acceleration
    if keys[pygame.K_UP]:
        if Car.CurrentVelocity > 0:
            Car.CurrentVelocity += Car.Acceleration * deltaTime
            if Car.CurrentVelocity > Car.MaxVelocity:
                Car.CurrentVelocity = Car.MaxVelocity
        else:
            Car.CurrentVelocity += 1.5 * Car.Acceleration * deltaTime
    elif keys[pygame.K_DOWN]:
        if Car.CurrentVelocity < 0:
            Car.CurrentVelocity -= Car.Acceleration * deltaTime
            if Car.CurrentVelocity < -Car.MaxVelocity:
                Car.CurrentVelocity = -Car.MaxVelocity
        else:
            Car.CurrentVelocity -= 1.5 * Car.Acceleration * deltaTime
    #------------

    #apply drag
    if Car.CurrentVelocity > Car.Drag * 2:
        Car.CurrentVelocity -= Car.Drag * deltaTime
    elif Car.CurrentVelocity < -Car.Drag * 2:
        Car.CurrentVelocity += Car.Drag * deltaTime
    else:
        Car.CurrentVelocity = 0
    #------------

    #decide rotation speed according to current and max velocity
    rotationMultiplier = 0
    if Car.CurrentVelocity > Car.MaxVelocity / 3:
        rotationMultiplier = (Car.MaxVelocity - Car.CurrentVelocity) / (Car.MaxVelocity / 2)
        if rotationMultiplier < 0.45:
            rotationMultiplier = 0.45
    else:
        rotationMultiplier = Car.CurrentVelocity / (Car.MaxVelocity / 3)
    #------------

    #rotate the car
    Car.Degree %= 360
    Car.MovingDegree %= 360

    if keys[pygame.K_LEFT]:
        Car.Degree += -Car.MaxRotation * rotationMultiplier
        if Car.Degree < 0:
            Car.Degree += 360
    elif keys[pygame.K_RIGHT]:
        Car.Degree += Car.MaxRotation * rotationMultiplier
        
    Car.MovingDegree = Car.Degree
    #------------

    Car.pos[0] += degree_to_position(Car.MovingDegree)[0] * Car.CurrentVelocity
    Car.pos[1] += degree_to_position(Car.MovingDegree)[1] * Car.CurrentVelocity
    
    # create polygon (a rectangle)
    draw_rectangle(Car.pos[0], Car.pos[1], Car.size[0], Car.size[1], (Car.R, Car.G, Car.B), Car.Degree)
    draw_rectangle(Car.pos[0], Car.pos[1], Car.size[0] * 1.5, Car.size[1] / 4, (50, 50, 200), Car.MovingDegree)
    
    pygame.display.flip()