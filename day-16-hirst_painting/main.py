import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
print(timmy.backward)
timmy.shape("turtle")
#timmy.color("red", "yellow")

colors = ['red', 'green', 'blue', 'yellow', 'black', 'brown', 'white']

size = 3
def shape(size):
    for i in range(size):
        angle = 360 / size
        timmy.right(angle)
        timmy.forward(100)

c_num = 0
for i in range(3, 10):
    timmy.color(colors[c_num])
    shape(i)
    c_num += 1

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# table = PrettyTable()
# table.add_column('Pokemon Name', ["Pikachu","Squirtle","Charmander"])
# table.add_column("Type", ['Electric', 'Water', 'Fire'])
# table.align = 'l'
# print(table)