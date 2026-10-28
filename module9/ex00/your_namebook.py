#!/usr/bin/env python3

def array_of_names(d):
  ret = []
  for x, y in d.items():
    ret.append(x.capitalize() + " " + y.capitalize())
  return ret

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
