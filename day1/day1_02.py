from numpy import floor

def required_fuel(fuel: int):
		return 0 if ( fuel < 7 ) else floor(fuel/3) -2 + required_fuel(floor(fuel/3) -2)


def all_fuel(fuels: list):
	with open('input.txt') as fuels:
		return sum(required_fuel(int(fuel)) for fuel in fuels.readlines())
