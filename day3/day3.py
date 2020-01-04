from typing import Set, Tuple

f = open(path)

if f.mode == "r":
	first, second = f.readlines()

def manhattan_dist(xy: Tuple) -> int:
	return abs(xy[0]) + abs(xy[1])

def locations(zmijug: str) -> Set[Tuple]:
	x = y = 0
	visited = set()

	for seg in zmijug.split(","):
		direction = seg[0]
		distance = int(seg[1:])

		for _ in range(distance):
			if direction == "U":
				y += 1
			elif direction == "D":
				y -= 1
			elif direction == "R":
				x += 1
			else:
				x -= 1

			visited.add((x,y))
	return visited

def intersection(zmijug1: str, zmijug2: str) -> Tuple:
	locations1 = locations(zmijug1)
	locations2 = locations(zmijug2)
	all = locations1.intersection(locations2) 
  
	return min(manhattan_dist(i) for i in all)

print(intersection(first, second))
f.close()
