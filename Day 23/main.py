import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score_board.scoreboard()
    car_manager.new_car()
    car_manager.movement()
    if player.ycor() == 280:
        score_board.update_score()
        player.goto(0, -280)
        car_manager.more_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()
