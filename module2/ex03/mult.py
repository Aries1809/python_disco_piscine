#!/usr/bin/env python3

if __name__ == "__main__":
    n1: int = int(input("Enter the first number: "))
    n2: int = int(input("Enter the second number: "))
    mult: int = n1 * n2
    print(f"{n1} x {n2} = {mult}")
    if mult > 0:
        print("The result is positive.")
    if mult < 0:
        print("The result is negative.")
    else: 
        print("The result is positive and negative.")
