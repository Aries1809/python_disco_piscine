#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l < 3:
  print("None")
else:
  while l != 1:
    print(f"{sys.argv[l - 1]}")
    l -= 1
