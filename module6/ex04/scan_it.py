#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l != 3:
  print("None")
else:
  print(f"{sys.argv[2].count(sys.argv[1])}")
