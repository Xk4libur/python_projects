#!/usr/bin/env python3

from datetime import datetime

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current = datetime.now().year
        return current - self.birth_year


# Ask dataa for user
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

person = Person(name, birth_year)
print(f"{person.name} is {person.age} years old.")