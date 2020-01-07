from numpy import floor
f = open(path, "r")

if f.mode == "r":
	input = f.readlines()

def required_fuel(fuels: list) -> int:
	#with open(path, "r") as fuels:
	#return sum(floor(int(fuel) / 3) - 2 for fuel in fuels.readlines())
	return sum(floor(int(fuel) / 3) - 2 for fuel in fuels)
f.close()
