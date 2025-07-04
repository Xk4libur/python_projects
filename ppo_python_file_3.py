#!/usr/bin/env python3

# Script with inheritance

class Animal:
    def __init__(self):
        print("The animal has been born.")

    def tail(self):
        print("The animal wags its tail.")

class Dog(Animal):
    def move(self):
        print("The dog is walking on its legs.")

my_dog = Dog()
my_dog.tail()
my_dog.move()