#!/usr/bin/env python3

i = int(input("Enter a number less than 25: "))
if i < 0:
  print("Error")
else:
  while i != 26:
    print(f"Inside the loop, my variable is {i}")
    i += 1
