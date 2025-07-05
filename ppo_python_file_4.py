#!/usr/bin/env python3

class Vehicle:
    def __init__(self, capacity, velocity, fuel):
        self.capacity = capacity
        self.velocity = velocity
        self.fuel = fuel

class Car(Vehicle):
    def move(self):
        print("\nThe car is moving.")

    def show_capacity(self):
        print(f"The car can carry {self.capacity} people.")

    def show_velocity(self):
        print(f"The car can move at {self.velocity} km/h.")

    def show_fuel(self):
        print(f"The car has {self.fuel} liters of fuel.\n")

class Train(Vehicle):
    def move(self):
        print("The train is moving.")

    def show_capacity(self):
        print(f"The train can carry {self.capacity} people.")

    def show_velocity(self):
        print(f"The train can move at {self.velocity} km/h.")

    def show_fuel(self):
        print(f"The train has {self.fuel} liters of fuel.\n")


class Airplane(Vehicle):
    def move(self):
        print("The airplane is flying.")

    def show_capacity(self):
        print(f"The airplane can carry {self.capacity} people.")

    def show_velocity(self):
        print(f"The airplane can move at {self.velocity} km/h.")

    def show_fuel(self):
        print(f"The airplane has {self.fuel} liters of fuel.")


print("\n [+] This script demonstrates inheritance and polymorphism with vehicles. \n")

my_car = Car(5, 120, 50)
my_car.move()
my_car.show_capacity()
my_car.show_velocity()
my_car.show_fuel()

my_train = Train(200, 400, 1400)
my_train.move()
my_train.show_capacity()
my_train.show_velocity()
my_train.show_fuel()

my_airplane = Airplane(300, 900, 3000)
my_airplane.move()
my_airplane.show_capacity()
my_airplane.show_velocity()
my_airplane.show_fuel()