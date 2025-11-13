#! /usr/bin/python3

f = open("2in.txt", "r")
c = f.read()

def count_chars(cin):
	d = {}
	for charry in cin:
		try:
			d[charry]+=1
		except KeyError:
			d[charry]=1
	return d

print(count_chars(c))
