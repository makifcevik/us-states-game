import turtle
import pandas as pd


data = pd.read_csv("50_states.csv")
STATE_COUNT = len(data)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=740, height=500)
screen.listen()
screen.onkey(key="Escape", fun=screen.bye)
screen.tracer(0)

image = "blank_states_img.gif"
screen.bgpic(image)


def write_state(pos_list):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.hideturtle()
    new_turtle.goto(pos_list[0][0], pos_list[0][1])
    new_turtle.color("black")
    new_turtle.write(arg=answer_state, align="center")


def check_answer(pos_list):
    # if the answer is correct
    if len(pos_list) != 0:
        # if the answer is new
        if answer_state not in right_answers:
            write_state(pos_list)
            right_answers.append(answer_state)


right_answers = []
missing_states = []
while len(right_answers) < STATE_COUNT:
    answer_state = screen.textinput(title=f"Guess The State {len(right_answers)}/50",
                                    prompt="What's another state?").title()

    if answer_state == "Exit":

        # finding missed states
        states = data["state"].values.tolist()
        for state in states:
            if state not in right_answers:
                missing_states.append(state)

        # creating a dataframe and a csv file out of missed states
        df = pd.DataFrame({"Missed States": missing_states})
        df.to_csv("states_to_learn.csv")
        print(df)
        print(f"You missed {len(missing_states)} in total.")
        break

    # get position values from the dataframe as a 2D list [[x, y]]
    pos = data[["x", "y"]][data["state"] == answer_state]
    pos_as_list = pos.values.tolist()
    check_answer(pos_as_list)
    if len(right_answers) == STATE_COUNT:

        turtle.hideturtle()
        turtle.write(arg="YOU WON!", align="center", font=("arial", 30, "bold"))
        turtle.penup()
        turtle.goto(0, -20)
        turtle.write(arg="You knew every state!", align="center", font=("arial", 15, "normal"))

    screen.update()

screen.exitonclick()
