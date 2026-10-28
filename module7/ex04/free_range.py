#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l != 3:
  print("None")
  exit()

x = int(sys.argv[1])
y = int(sys.argv[2])

if x >= y:
  print("Input error")
  exit()

ls = []

for n in range(0, (y - x + 1)):
  ls.append(x + n)
print(f"{ls}")
