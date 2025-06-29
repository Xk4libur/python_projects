#!/usr/bin/python3

print(f""" 
 __  __       _ _   _                              _             
|  \/  |_   _| | |_(_)   ___  _ __   ___ _ __ __ _| |_ ___  _ __ 
| |\/| | | | | | __| |  / _ \| '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |  | | |_| | | |_| | | (_) | |_) |  __/ | | (_| | || (_) | |   
|_|  |_|\__,_|_|\__|_|  \___/| .__/ \___|_|  \__,_|\__\___/|_|   
                             |_|                                 
                                                                    made by xk4libur
""")

print("\nWhich operation do you want to perform?")

print("\n 1) Addition operation\n")
print("\n 2) Substract operation\n")
print("\n 3) Multiplication operation\n")
print("\n 4) Split operation\n")
print("\n 5) Exponent operation\n")

choice = input("Choose here: ")

if choice == "1":
    print("\n[+] Which numbers do you want to add? (separated by spaces)\n")
    numbers = input().split()
    try:
        total = sum(int(num) for num in numbers)
        print(f"\nThe result of the operation is: {total} \n")
    except ValueError:
        print("\nPlease enter valid numbers.")