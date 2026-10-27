#!/usr/bin/env python3

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []

for n in l1:
  if n > 5:
    l2.append(n + 2)

print(f"{l1}")
print(f"{l2}")
