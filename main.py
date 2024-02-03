#!/bin/python3
#gfdklj;gslkfdgj
#Import library code
from p5 import *
from random import randint

#Setup global variables
screen_size = 400
rocket_y = screen_size
burn = 100
orbit_radius = 250
orbit_y = screen_size - orbit_radius

#The draw_rocket function goes here
def draw_rocket():
  global rocket_y, fuel, burn

  if fuel >= burn and rocket_y > orbit_y:
    rocket_y -= 1
    fuel -= burn
    print('Fuel Left: ', fuel)

    no_stroke()

    for i in range(25):
      fill (255, 255 - i10, 0)
      ellipse(width/2, rocket_y + i, 8, 3)

    fill(200, 200, 200, 100)
    for i in range(20):
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
  rocket_y -= 1
  fuel -= 1
  print('Fuel left: ', fuel)
  no_stroke()
  for i in range(25):
    fill(255, 255 - i 10, 0)
    ellipse(width/2, rocket_y + i, 8, 3)

  fill(200, 200, 200, 100)
  for i in range(20):
    ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  if fuel < burn and rocket_y > orbit_y:
    tint(255, 0, 0)

  elif rocket_y <= orbit_y:
    tint(0, 255, 0)
  image(rocket, width/2, rocket_y,  64, 64)
  no_tint()

#The draw_background function goes here
def draw_background():
  background(0)
  image(planet, width/2, height, 300, 300)

  no_fill()
  stroke(255)
  stroke_weight(2)
  ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)


def setup():
  # Setup your animation here
 size(screen_size, screen_size)
 image_mode(CENTER)
 global planet, rocket
 global planet
 planet = load_image('purple_plan.png')
 rocket = load_image('rocket.png')


def draw():
  # Things to do in every frame
  draw_background()
  draw_rocket()



fuel = int(input('How many gallons of fuel must we use?'))
run()