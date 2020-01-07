from functools import reduce
from numpy import floor
f = open(path, "r")

if f.mode == "r":
	input = f.readlines()

def required_fuel(fuels: list) -> int:
	sum = 0
	for fuel in fuels:
		sum += floor(int(fuel)/3) - 2
	return sum

f.close()
