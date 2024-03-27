from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager():
    
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = 5

    
    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)
        
    
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    

    def increase_speed(self):
        self.car_speed += 10

