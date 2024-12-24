import turtle
import math

t = turtle.Turtle()


#set up a screen
s = turtle.Screen()
s.bgcolor("green")

#draw a circle
t.pensize(4)
t.right(150)
t.penup()
t.forward(30)
t.pendown()
t.circle(150)
t.color("black")
t.shape("turtle")
t.hideturtle()


def drawCircle(radius):
    circumference = 2 * math.pi * radius
    step_size = circumference / 360


turtle.done()
