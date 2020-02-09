import math
with open('input.txt') as f:
    universe = f.readlines()

asteroids = {}
x, y = 0, 0
for row in universe:
    for element in row:
        x+=1
        if element == '#':
            asteroids[(x,y)] = set() # we will match one asteroid with multiple values
    y+= 1
    x = 0

'''
Matching every asteroid with the asteroid it has in sight ( its angle ). 
Matching with a set in order to match more that one asteroid, but having only unique values, that
will remove two occurrances of the same angle, which means we will only have one asteroid within one angle.
'''
for asteroid1 in asteroids:
    for asteroid2 in asteroids:
        if asteroid1 == asteroid2: # skip if coincide
            continue

        #Return the arc tangent (measured in radians) of y/x.
        #Unlike atan(y/x), the signs of both x and y are considered
        angle = math.atan2(asteroid2[1] - asteroid1[1], asteroid2[0] - asteroid1[0])*180/math.pi   # rad2deg7
        asteroids[asteroid1].add(angle)

winner = max(asteroids.values(), key=len) #key=len indicates we are looking for the most matched planets (set length)
print(len(winner))
