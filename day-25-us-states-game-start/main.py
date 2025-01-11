import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Easily get coordinates by mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State",
                                    prompt="What's another State's name: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_guesses]
        # missing_states = []
        # for state in state_list:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_date = data[data.state == answer_state]
        t.goto(int(row_date.x), int(row_date.y))
        t.write(answer_state, align="left", font=("Courier", 10, "normal"))


