#!/usr/bin/env python3

import sys

def shrink(s):
  cnt = 0
  while cnt != 8:
    print(f"{s[cnt]}", end="")
    cnt += 1
  print("")

def enlarge(s):
  cnt  = len(s)
  print(f"{s}", end="")
  while cnt != 8:
    print("Z", end="")
    cnt += 1
  print("")

l = len(sys.argv)

if l == 1:
  print("None")
  exit()

for n in range(1, l):
  if len(sys.argv[n]) > 8:
    shrink(sys.argv[n])
  if len(sys.argv[n]) < 8:
    enlarge(sys.argv[n])
  if len(sys.argv[n]) == 8:
    print(f"{sys.argv[n]}")

