#!/bin/python3

# Import library code
from p5 import *
from random import randint
from math import sqrt
from math import atan

# Setup global variables
screen_size = 400
rocket_y = screen_size  # Start at the bottom
burn = 100  # How much fuel is burned in each frame
orbit_radius = 250
orbit_y = screen_size - orbit_radius
rocket_x = screen_size/2
high_orbit_radius = 350
high_orbit_y = screen_size - high_orbit_radius
speed = 1  # How far the rocket flies each frame
itiration = 0
fuel = 0
planet2_x = 0
planet2_y = 0
angle = 0
distance = 0


def generate_moon_cords():
    global planet2_x, planet2_y, distance, angle
    temp_planet_x = 0
    planet2_x = randint(30,screen_size-30)
    planet2_y = randint(30,screen_size/2)
    if planet2_x < screen_size/2:
        temp_planet_x = (screen_size/2) - planet2_x
    elif planet2_x > screen_size/2:
        temp_planet_x = planet2_x - (screen_size/2)
        
    distance = sqrt(planet2_x^2+temp_planet_x^2)
    
    angle = atan(planet2_y/temp_planet_x)

def set_vars():
    global fuel, burn, speed
    fuel = int(input('How many kilograms of fuel do you want to use?'))
    burn = int(input('How much fuel should the rocket burn each frame?'))
    speed = int(input('How far should the rocket travel each frame?'))

# The draw_rocket function goes here
def draw_rocket():
    global rocket_y, rocket_x, fuel, burn, angle, distance
    
    if fuel >= burn and rocket_y > high_orbit_y:  # Still flying
        rocket_y -= speed  # Move the rocket
        rocket_x -= .1
        fuel -= burn  # Burn fuel
        print('Fuel left: ', fuel)
      
        no_stroke()  # Turn off the stroke
      
        for i in range(25):  # Draw 25 burning exhaust ellipses
            fill(255, 255 - i*10, 0)  # yellow
            ellipse(rocket_x, rocket_y + i, 8, 3)  # i increases each time the loop repeats
        
        fill(200, 200, 200, 100)  # transparent grey
        
        for i in range(20):  # draw 20 random smoke ellipses
            ellipse(rocket_x + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
      
    if fuel < burn and rocket_y > high_orbit_y:  # No more fuel and not in orbit
        tint(255, 0, 0)  # Failure
    elif rocket_y <= orbit_y and rocket_y > high_orbit_y:
        tint(0, 255, 0)  # Success
    elif fuel < 1000 and rocket_y <= high_orbit_y:
        tint(0, 100, 200)  # High orbit success
    elif fuel >= 1000 and rocket_y <= high_orbit_y: 
        tint(255, 200, 0)  # Too much fuel
    
    image(rocket, rocket_x, rocket_y, 64, 64)
    no_tint()

    if fuel <= 0:
        exit()
  

# The draw_background function goes here
def draw_background():
    global planet2_x, planet2_y
    background(0)  # Short for background(0, 0, 0) - black 
    image(planet, width/2, height, 300, 300)  # draw the image
    image(planet2, planet2_x, planet2_y ,100,100)
    print(height)
    
    # Draw the lower orbit
    no_fill()  # Turn off any fill
    stroke(255)  # Set a white stroke
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius*2, orbit_radius*2)
    
    # Draw the higher orbit
    stroke(0, 100, 200)  # Set a bluish stroke
    stroke_weight(2)
    ellipse(width/2, height, high_orbit_radius*2, high_orbit_radius*2)


def setup():
    # Setup your animation here 
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket, planet2
    planet = load_image('orange_planet.png')  # Your chosen planet
    rocket = load_image('rocket.png')
    planet2 = load_image('moon.png')


def draw():
    draw_background()  
    draw_rocket()

generate_moon_cords()
set_vars()
run()
