#! /usr/bin/python3

import re

r2 = re.compile("[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]")

f = open("3in.txt", "r")
c = f.read()

print("".join([x[4] for x in r2.findall(c)]))
