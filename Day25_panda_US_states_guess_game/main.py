import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.setup(width=700, height=600)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50 States correct",
                                   prompt="What's another state's name?").capitalize()

    if user_answer == "Exit":
        missing_states = []
        for states in guessed_state:
            if states not in guessed_state:
                missing_states.append(states)
        remaining_states = pandas.DataFrame(missing_states)
        remaining_states.to_csv("States_to_learn.csv")
        break
    if user_answer in state_list:
        guessed_state.append(user_answer)
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        state_data = data[data.state == user_answer]
        tom.goto(int(state_data.x), int(state_data.y))
        tom.write(user_answer)


# screen.exitonclick()
# screen.mainloop()
