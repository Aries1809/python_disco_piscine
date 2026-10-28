#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l < 2:
  print("None")
else:
  print(f"parameters: {l - 1}")
  for n in range(1, l):
    print(f"{sys.argv[n]}: {len(sys.argv[n])}")
