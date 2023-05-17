from turtle import *
from random import *

#setup
speed (50)
Screen().bgcolor("black")
hideturtle()

#get screen size
width = window_width()
height = window_height()

#draw stars at random positions
def draw_star (xpos, ypos):
    size = randrange(4, 10)

    #move pen to set position
    penup()
    goto(xpos, ypos)
    pendown()

    #draw the star
    dot(size, "white")

#plot random stars
for x in range(100):
    xpos = randrange(round(-width/2), round(width/2))
    ypos = randrange(round(-height/2), round(height/2))

    draw_star(xpos, ypos)

#keep window open
done()