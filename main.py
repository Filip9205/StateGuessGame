import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)
map_turtle.penup()
map_turtle.goto(0, 0)

writer_turtle = turtle.Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()


data = pandas.read_csv("50_states.csv")

correct_guess = 0
states_to_guess = data.states.tolist()
guessed_states = []


while correct_guess != 50:
    answer = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?").capitalize()
    if answer == "Exit":
        states_to_learn = []
        for state in states_to_guess:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states.to_learn.csv")

        break

    if answer in states_to_guess and answer not in guessed_states:
        guessed_states.append(answer)
        correct_guess += 1
        state_data = data[data["state"] == answer]
        x, y = int(state_data["x"]), int(state_data["y"])
        writer_turtle.goto(x, y)
        writer_turtle.write(answer, align="center", font=("Arial", 10, "bold"))



turtle.exitonclick()
