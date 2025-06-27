#!/usr/bin/env python3

import random
secret_num = random.randint(1,20)
attempt = 0

try:
    while attempt != secret_num:
        user_num = int(input("Put a number between 1 and 20: "))

    if user_num < secret_num:
        print("\nToo low.\n")
    
    elif user_num > secret_num:
        print("\nToo big.\n")

    else user_num == secret_num:
         print("\nGood number\n")

except KeyboardInterrupt:
    print("\n[+] Leaving the program\n")