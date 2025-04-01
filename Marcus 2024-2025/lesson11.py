# Objective:
# Create a Car class in Python that models the basic attributes and behaviors of a car. Your class should include:

# An initializer (__init__ method) to set up a car's attributes
# Methods for car actions (e.g., starting, stopping, accelerating, braking)
# A method to display car details

# Tasks:
# 1. Define the Car Class
# Create a class named Car with the following attributes:

# make (str) → The brand of the car (e.g., "Toyota")
# model (str) → The model of the car (e.g., "Corolla")
# year (int) → The year the car was manufactured
# color (str) → The color of the car
# speed (int, default = 0) → The current speed of the car

# 2.  Implement the Following Methods:
# start_engine() → Prints "The engine is now running."
# stop_engine() → Prints "The engine is off." and sets speed to 0
# accelerate(amount) → Increases speed by amount and prints the new speed
# brake(amount) → Decreases speed by amount but doesn’t go below 0
# get_info() → Returns a formatted string with car details

class Car:
    def __init__(self, make, model, colour, year, speed=0):
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.speed = max(speed, 0) # this ensures we can't initialise a negative value

    def get_info(self):
        return f"The car is a {self.model} made by {self.make}, it is {self.colour} in colour and made in {self.year}."

    def get_speed(self):
        return f"The {self.make} {self.model} is currently travelling at {self.speed} km per hour."

    def accelerate(self, amount):
        self.speed += amount
        pass

    def brake(self, amount):
        self.speed -= amount
        self.speed = max(0, self.speed)
        pass

# Show me how to initialise the class
# c1 = Car("Toyota", "Corolla", "Red", 2022)
# print(c1.get_info())
# print(c1.get_speed())
# c1.accelerate(20)
# print(c1.get_speed())
# c1.brake(30)
# print(c1.get_speed())
# c2 = Car("Honda", "Civic", "Gray", 2008, 15)
# print(c2.get_speed())
# c3 = Car("Nissan", "GTR", "Blue", 2015, -15)
# print(c3.get_speed())


class Bicycle:
    def __init__(self, colour, owner, speed=0):
        self.colour = colour
        self.owner = owner
        self.speed = max(speed, 0)
    
    # def __str__(self):
    #     return "The bicycle is HERE"

    def get_info(self):
        # The bicycle is Red and owned by Samuel.
        return f"The bicycle is owned by {self.owner} and it is {self.colour}"

    def get_speed(self):
        # The bicycle owned by Samuel is travelling at 0 km per hour.
        return f"The bicycle is currently travelling at {self.speed} km per hour, it is owned by {self.owner}"

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        self.speed = max(self.speed, 0)

    def change_owner(self, new_owner):
        old_owner = self.owner
        self.owner = new_owner
        return f"The bicycle has changed owners from {old_owner} to {self.owner}"

b1 = Bicycle("Red", "Samuel")
# print(b1)
print(b1.get_info())
print(b1.get_speed())
b1.accelerate(10)
print(b1.get_speed())
b1.brake(5)
print(b1.get_speed())
b1.brake(10)
print(b1.get_speed())
print(b1.change_owner("Mark"))
print(b1.get_info())
# b2  = Bicycle("Green", "Marcus", 15)