#!/usr/bin/env python3

import sys

def downcase_it(s):
  ret = s.lower()
  return ret

l = len(sys.argv)

if l < 2:
    print("None")
    exit()

for n in range(1, l):
    print(f"{downcase_it(sys.argv[n])}")
