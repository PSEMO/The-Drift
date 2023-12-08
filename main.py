import pygame
import random
import math
import numpy as np
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
    size = [54, 22]
    CurrentVelocity = 0
    MaxVelocity = 10
    Degree = 0
    #Constant variables
    MaxRotation = 1
    Drag = 0.00025
    Acceleration = 0.0005
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

Car = car()

#Update()
while 1:
    #count the time frame took and assign it to ms
    ms = clock.tick(framerate)
    deltaTime = ms * 10

    #resets screen
    screen.fill((100, 100, 100))

    #detect events including inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # get the user input
    keys = pygame.key.get_pressed()
    # set the car acceleration and angular velocity based on the keys
    if keys[pygame.K_UP]:
        if car.CurrentVelocity > 0:
            car.CurrentVelocity += car.Acceleration * deltaTime
            if car.CurrentVelocity > car.MaxVelocity:
                car.CurrentVelocity = car.MaxVelocity
        else:
            car.CurrentVelocity += 1.5 * car.Acceleration * deltaTime
    elif keys[pygame.K_DOWN]:
        if car.CurrentVelocity < 0:
            car.CurrentVelocity -= car.Acceleration * deltaTime
            if car.CurrentVelocity < -car.MaxVelocity:
                car.CurrentVelocity = -car.MaxVelocity
        else:
            car.CurrentVelocity -= 1.5 * car.Acceleration * deltaTime

    if car.CurrentVelocity > car.Drag * 2:
        car.CurrentVelocity -= car.Drag * deltaTime
    elif car.CurrentVelocity < -car.Drag * 2:
        car.CurrentVelocity += car.Drag * deltaTime
    else:
        car.CurrentVelocity = 0

    rotationMultiplier = 0
    if car.CurrentVelocity > car.MaxVelocity / 2:
        rotationMultiplier = (car.MaxVelocity - car.CurrentVelocity) / (car.MaxVelocity / 2)
        if rotationMultiplier < 0.3:
            rotationMultiplier = 0.3
    else:
        rotationMultiplier = car.CurrentVelocity / (car.MaxVelocity / 2)
    
    if keys[pygame.K_LEFT]:
        car.Degree += -car.MaxRotation * rotationMultiplier
    elif keys[pygame.K_RIGHT]:
        car.Degree += car.MaxRotation * rotationMultiplier
    else:
        car.CurrentRotation = 0

    car.Degree %= 360
    _carDegree = math.radians(car.Degree)
    car.pos[0] += degree_to_position(car.Degree)[0] * car.CurrentVelocity
    car.pos[1] += degree_to_position(car.Degree)[1] * car.CurrentVelocity
    
    # create polygon (a rectangle)
    draw_rectangle(Car.pos[0], Car.pos[1], Car.size[0], Car.size[1], (Car.R, Car.G, Car.B), car.Degree)
    
    pygame.display.flip()