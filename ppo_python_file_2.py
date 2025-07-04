#!/usr/bin/env python3

# Script with decorator

def decorator(func):
    def modified_function():
        print(f"\n- Pre-function execution\n")
        func()
        print(f"\n- Post-function execution\n")
    return modified_function

@decorator
def install():
    print(f"\n[+] Installing package...\n")

install()