import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("red")
c = 0
d = 0
# To increase speed
t.speed(0)
# create a square
while True:
    for i in range(4):
        t.forward(80)
    t.right(90)
    t.right(15)
    c += 1

    # To break the drawing:
    if c >= 390 / 15:
        t.forward(50)
    c = 0
    d += 1
    if d >= 12:
        break
t.hideturtle()
s.exitonclick()
