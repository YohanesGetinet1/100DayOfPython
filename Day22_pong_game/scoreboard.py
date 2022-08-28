from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 220)
        self.write(self.left_score, align="center", font=("Courier", 55, "normal"))
        self.goto(100, 220)
        self.write(self.right_score, align="center", font=("Courier", 55, "normal"))

    def left_scoreboard(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def right_scoreboard(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
