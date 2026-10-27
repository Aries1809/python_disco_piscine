#!/usr/bin/env python3

x = 0

while x != 11:
  y = 0
  print(f"Table of {x}:", end=" ")
  while y!= 11:
    print(f"{x * y}", end=" ")
    y += 1
  print("")
  x += 1
