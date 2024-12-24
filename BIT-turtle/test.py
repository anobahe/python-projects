import turtle
from turtle import Turtle, Screen
#from prettytable import PrettyTable
import random

timmy = Turtle()
timmy.shape("turtle")
#timmy.color("red", "yellow")
turtle.colormode(255)

def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# direction = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed(0)

# for i in range(200):
#     timmy.color(rgb_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

for i in range(200):
    timmy.color(rgb_color())
    timmy.right(1)
    timmy.circle(100)




my_screen = Screen()
#print(my_screen.canvheight)
my_screen.exitonclick()