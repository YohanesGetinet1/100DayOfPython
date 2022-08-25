import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_choice = screen.textinput(title="Make your bet on the turtle",
                               prompt=f"Which turtle will win the race?\n {colors}\n "
                                      f"                  choose the color ")

y_coordinate = [-100, -50, 0, 50, 100, 150]
is_race_started = False
turtles_to_race = []
for x in range(0, 6):
    """simple for loop that simplify code redundancy which is commented out below """
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(x=-230, y=y_coordinate[x])
    turtles_to_race.append(new_turtle)

if user_choice:
    is_race_started = True

while is_race_started:

    for x in turtles_to_race:
        if x.xcor() > 235:
            is_race_started = False
            winner = x.pencolor()
            if winner == user_choice:
                print(f"You won the winner is {winner}")
            else:
                print(f"You lose the winner is {winner}")
        distance_move = random.randint(0, 10)
        x.forward(distance_move)

# tim1 = Turtle("turtle")
# tim2 = Turtle("turtle")
# tim3 = Turtle("turtle")
# tim4 = Turtle("turtle")
# tim5 = Turtle("turtle")
# tim6 = Turtle("turtle")
#
# tim1 .color("red")
# tim2 .color("orange")
# tim3 .color("yellow")
# tim4 .color("green")
# tim5 .color("blue")
# tim6 .color("purple")
#
# tim1.penup()
# tim1.goto(x=-230, y=-100)
# tim2.penup()
# tim2.goto(x=-230, y=-50)
# tim3.penup()
# tim3.goto(x=-230, y=0)
# tim4.penup()
# tim4.goto(x=-230, y=50)
# tim5.penup()
# tim5.goto(x=-230, y=100)
# tim6.penup()
# tim6.goto(x=-230, y=150)

screen.exitonclick()
