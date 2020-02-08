from numpy import floor
def required_fuel():
	with open('input.txt') as fuels:
		return sum( floor(int(fuel) / 3) - 2 for fuel in fuels.readlines() )
