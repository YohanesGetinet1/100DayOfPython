from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.snake_create()
        self.head = self.segment[0]

    def snake_create(self):
        """This function creates snake"""

        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segment.append(new_snake)

    def snake_extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for snake_number in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[snake_number - 1].xcor()
            new_y = self.segment[snake_number - 1].ycor()
            self.segment[snake_number].goto(new_x, new_y)
        self.head.forward(DISTANCE_MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
