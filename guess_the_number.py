#!/usr/bin/env/python3

import random
secret_num = random.randint(1,20)
user_num = 0

while attempt != secret_num:
user_num = int(input("Put a number: "))

    if user_num < secret_num:
        print("Too low.")
    
    elif user_num > secret_num:
        print("Too big.")

print("Good number")