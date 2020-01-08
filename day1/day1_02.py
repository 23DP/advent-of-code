from numpy import floor

def required_fuel(fuel: int) -> int:
	if fuel < 7:
		return 0
	else:
		return floor(fuel/3) -2 + required_fuel(floor(fuel/3) -2)

def all_fuel(fuels: list) -> int:
	with open(path, "r") as fuels:
		return sum(required_fuel(int(fuel)) for fuel in fuels.readlines())
