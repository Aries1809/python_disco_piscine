#!/usr/bin/env python3

if __name__ == "__main__":
    pwd: str = "bru"
    inp: str = input("Enter password: ")
    if inp == pwd:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
