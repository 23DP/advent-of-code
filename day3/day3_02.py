from typing import  Tuple, Dict, Set

f = open(path)

if f.mode == "r":
	first, second = f.readlines()


def locations(zmijug: str) -> Dict[Tuple, int]:
	x = y = steps = 0
	visited = {}

	for seg in zmijug.split(","):
		direction = seg[0]
		distance = int(seg[1:])

		for _ in range(distance):
			steps += 1
			if direction == "U":
				y += 1
			elif direction == "D":
				y -= 1
			elif direction == "R":
				x += 1
			else:
				x -= 1
				
			c = (x,y)
			if c not in visited:
				visited[c] = steps
	
	return visited

def intersections(zmijug1: str, zmijug2: str) -> int:
	locations1 = locations(zmijug1)
	locations2 = locations(zmijug2)
	inters = set(locations1.keys()).intersection(set(locations2.keys()))

	return min(locations1[i] + locations2[i] for i in inters)

print(intersections(first, second))
f.close()
