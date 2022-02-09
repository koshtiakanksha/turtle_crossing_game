from turtle import Screen
from tim import Tim
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()
tim = Tim()
screen.onkey(tim.move_forward, "Up")
car = Cars()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.car_forward()

    for i in car.all_cars:
        if i.distance(tim) < 20:
            scoreboard.game_over()
            game_on = False

    if tim.ycor() == 250:
        tim.reset_tim()
        car.level_up()
        scoreboard.update_level()

screen.exitonclick()
