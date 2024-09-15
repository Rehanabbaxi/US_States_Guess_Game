import turtle
import  pandas as pd
FONT = ("Courier", 10, "normal")

## tuetle object for maping states name on map
prompt_turtle = turtle.Turtle()
prompt_turtle.penup()
prompt_turtle.hideturtle()

screen = turtle.Screen()
screen.title("US States")
iamge = "blank_states_img.gif"
screen.addshape(iamge)
turtle.shape(iamge)

data = pd .read_csv("50_states.csv")
states_list  = data.state.to_list()

correct_guessed_states = []
scores = 0

while len(correct_guessed_states) < len(states_list):
    heading = f"{scores}/50 are correct states "
    user_answer = screen.textinput(title= heading , prompt="Gues another state name ?")
    user_answer = user_answer.title()

    if user_answer in states_list and user_answer not in correct_guessed_states:
        x = data[data["state"] == user_answer]["x"].values[0]
        y = data[data["state"] == user_answer]["y"].values[0]

        prompt_turtle.goto(x, y)
        prompt_turtle.write(user_answer, align ="center", font= FONT)
        correct_guessed_states.append(user_answer)
        scores += 1


screen.exitonclick()