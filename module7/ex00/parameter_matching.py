#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l != 2:
  print(None)
else:
  s = input("What was the parameter? ")
  if s == sys.argv[1]:
    print("Good job!")
  else:
    print("Nope, sorry...")
