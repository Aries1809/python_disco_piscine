#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l != 2:
  print("None")
else:
  print(f"{sys.argv[1].lower()}")
