import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable
import random

# import colorgram   ######Extract color from images#####
# rgb_color = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
# print(rgb_color)


rgb_color = [(243, 234, 76), (211, 158, 93), (188, 12, 69),(111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166),
     (160, 78, 35), (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95),
     (234, 165, 194), (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95),
     (135, 213, 228), (9, 102, 63), (134, 36, 21), (93, 29, 12), (156, 211, 190)]

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(rgb_color))
    timmy.forward(50)

    if count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


my_screen = Screen()
my_screen.exitonclick()