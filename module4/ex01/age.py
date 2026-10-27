#!/usr/bin/env python3

i = int(input("Please tell me your age: "))
print(f"You are currently {i} years old.")
cnt = 10
while cnt != 40:
  print(f"In {cnt} years, you'll be {i + cnt} years old.")
  cnt += 10
