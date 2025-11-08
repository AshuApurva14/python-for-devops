#!/usr/bin/env python


# Using for loop in python

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)


env = ["dev"]

for y in env:
    if y == "dev":
      ENV=y
    if y == "test":
      ENV=y
    if y == "uat":
      ENV=y
    if y == "qa":
      ENV=y
    if y == "prod":
      ENV=y

print(ENV)

