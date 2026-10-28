#!/usr/bin/env python3

def hello(nm="noble stranger"):
  if isinstance(nm, str) == False:
    print("Error! It was not a name.")
    exit()
  print(f"Hello, {nm}.")

s = input("Enter your name: ")
if (s == "no") or (s == ""):
  hello()
else:
  hello(s)
