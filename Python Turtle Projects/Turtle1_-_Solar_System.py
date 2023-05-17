from turtle import *

#set screen size
Screen().setup(800, 500)

#set turtle speed
speed(10)

#background colour
Screen().bgcolor("black")

#first planet 
color("orange")
begin_fill()
circle(60)
end_fill()

#move pen
penup()
forward(100)
pendown()

#second planet 
color("gray")
begin_fill()
circle(20)
end_fill()

#move pen
penup()
forward(90)
pendown()

#third planet 
color("green")
begin_fill()
circle(30)
end_fill()

#keep window open
done()