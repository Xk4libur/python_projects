#!/usr/bin/env python3

print(r"""
  ___          _                      _ _     _   
 / _ \ _ __ __| | ___ _ __    __ _   | (_)___| |_ 
| | | | '__/ _` |/ _ \ '__|  / _` |  | | / __| __|
| |_| | | | (_| |  __/ |    | (_| |  | | \__ \ |_ 
 \___/|_|  \__,_|\___|_|     \__,_|  |_|_|___/\__|
                                                    made by xk4libur
 """)

print("\nGive me some numbers (separated by spaces): \n")

a = input(">> ")

try:
    numbers = [int(n) for n in a.split()]
    print("\nThe list of numbers is:", numbers)
except ValueError:
    print("\nInclude only numbers between the spaces.")
except KeyboardInterrupt:
    print("\n[+] Leaving the program\n")
