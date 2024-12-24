from turtle import Turtle
import math

t = turtle.Turtle()


#set up a screen
s = turtle.Screen()
s.bgcolor("green")
t.speed(0)
#draw a circle
t.pensize(4)
t.pendown()
#t.circle(50)
t.shape("turtle")



def drawCircle(radius):
    circumference = 2 * math.pi * radius
    step_size = circumference / 360
    for i in range(360):
        t.forward(step_size)
        t.left(1)


# t.speed(0)
# drawCircle(40)
# t.speed(0)
# t.color("red")
# drawCircle(60)
# t.speed(0)
# t.color("blue")
# drawCircle(80)
# t.speed(0)


colors = ['red', 'green', 'blue', 'yellow', 'black', 'brown', 'white']
num = 100
for i in range(7):
    num -= 10
    drawCircle(num)
    t.color(colors[i])

t.hideturtle()
turtle.done()
