from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "orange", "blue", "purple"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_pace = 5

    def generate_car(self):
        random_choice = random.randint(1, 8)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            y = random.randint(-200, 200)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def car_forward(self):
        for i in self.all_cars:
            i.forward(self.car_pace)

    def level_up(self):
        self.car_pace += 2
