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
    print(f"Resultado: {number_1 + number_2}")
elif operator == "-":
    print(f"Resultado: {number_1 - number_2}")
elif operator == "*":
    print(f"Resultado: {number_1 * number_2}")
elif operator == "/":
    if b != 0:
        print(f"Resultado: {number_1 / number_2}")
    else:
        print("Error: división por cero.")
else:
    print("Operador no válido.")