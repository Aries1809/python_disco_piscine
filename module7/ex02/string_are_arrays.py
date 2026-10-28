#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l != 2:
  print("None")
else:
  z = sys.argv[1].count("z")
  if z == 0:
    print("None")
  else:
    while (z != 0):
      print("z", end="")
      z -= 1
    print("")

