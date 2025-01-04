from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
terry = Turtle()
t = Turtle()
screen = Screen()
tim.shape("turtle")


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def reset():
    tim.reset()


screen.listen()
#keys = ['w', 's', 'a', 'd']

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)



screen.exitonclick()