import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.random_car()
    car_manager.move_cars()
    # detect collision of cars
    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    # detect when the player reach the finishing line
    if player.reached_destination():
        player.new_game()
        car_manager.level_upgrade()
        scoreboard.level_increase()

screen.exitonclick()
