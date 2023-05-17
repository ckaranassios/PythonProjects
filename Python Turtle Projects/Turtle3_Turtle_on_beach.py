from turtle import *
from random import *

#setup
speed (50)
Screen().setup(800, 500)
Screen().bgcolor("#FFB133")

#draw background
penup()
goto(100, 200)
pendown()

color("#36CDE3")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

penup()

#centre turtle
goto(-200, 0)
shape("turtle")
color("green")
move_distance = 20

#movement functions
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

#win condition
def check_goal():
    if xcor() > 100:
        hideturtle()
        color("white")
        write("You win!")
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

#controlling the turtle
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")

#waiting for input
listen()

#keeping the window open
done()