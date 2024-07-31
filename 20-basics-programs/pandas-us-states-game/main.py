import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
caption = turtle.Turtle()
caption.penup()
caption.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state

guessed_state = []
count_states = len(states)

while len(guessed_state) != count_states:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{count_states} States Correct",
                                    prompt="What another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if answer_state == state and state not in guessed_state:
            x = int(data[data['state'] == state].x)
            y = int(data[data['state'] == state].y)
            caption.goto(x, y)
            caption.write(state)
            guessed_state.append(state)
            #states = data.drop(data[data['state'] == state].index)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()




