from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
right_paddle = Paddle()
left_paddle = Paddle()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("pong")
ball = Ball()


right_paddle.create_paddle((350, 0))
left_paddle.create_paddle((-350, 0))


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    # detect the collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_scoreboard()

    # detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_scoreboard()

screen.exitonclick()
