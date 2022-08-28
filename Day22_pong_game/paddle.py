from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self, position):
        for number_of_paddle in range(2):
            self.penup()
            self.shape(name="square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.color("white")
            self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
