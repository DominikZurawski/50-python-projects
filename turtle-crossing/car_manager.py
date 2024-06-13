from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def random_position():
    pos = (random.randint(300, 340), random.randint(-250, 250))
    return pos


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle('square')
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(random_position())
            self.cars.append(car)


    def cars_move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

