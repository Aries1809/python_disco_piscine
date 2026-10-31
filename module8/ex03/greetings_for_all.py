#!/usr/bin/env python3

def greetings(nm="noble stranger"):
  if isinstance(nm, str) == False:
    print("Error! It was not a name.")
    return()
  print(f"Hello, {nm}.")

s = input("Enter your name: ")
if (s == "no") or (s == ""):
  greetings()
else:
  greetings(s)
