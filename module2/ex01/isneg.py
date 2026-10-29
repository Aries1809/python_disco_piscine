#!/usr/bin/env python3

if __name__ == "__main__":
    num: int = int(input("Enter a number: "))
    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
