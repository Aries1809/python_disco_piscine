#!/usr/bin/env python3

import sys

l = len(sys.argv)

if l < 2:
  print("None")
else:
  for n in range(1, l):
    if sys.argv[n].endswith("ism"):
      pass
    else:
      print(f"{sys.argv[n]}ism")
