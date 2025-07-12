#!/usr/bin/env python3

print(r""" 
 __  __ _       _             _      
|  \/  (_)_ __ (_)   ___ __ _| | ___ 
| |\/| | | '_ \| |  / __/ _` | |/ __|
| |  | | | | | | | | (_| (_| | | (__ 
|_|  |_|_|_| |_|_|  \___\__,_|_|\___|
                                            made by xk4libur
""")

number_1 = float(input("Put the first number: "))
number_2 = float(input("Put the second number: "))

print("\nAvailable operations: +, -, x, /\n")
operator = input("Vhoose your option: ")

if operator == "+":
    print(f"\nResultado: {number_1 + number_2}\n")
elif operator == "-":
    print(f"\nResultado: {number_1 - number_2}\n")
elif operator == "*":
    print(f"\nResultado: {number_1 * number_2}\n")
elif operator == "/":
    if b != 0:
        print(f"\nResultado: {number_1 / number_2}\n")
    else:
        print("\nError: división por cero.\n")
else:
    print("Operador no válido.")