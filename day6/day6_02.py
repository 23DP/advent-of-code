f = open(path, "r")

if f.mode == "r":
	all_orbits = f.readlines()

pairs = {}
connections = 0

def orbits(dict, key, target):
    AAA = dict[key]
    cnt = 1 #Count in the orbit around the target planet

    while AAA != target:     #count how many pairs is key from target
        cnt += 1
        BBB = AAA
        AAA = dict[BBB]

    return cnt


# COM ) AAA ) BBB
for i in range(len(all_orbits)):
    AAA = all_orbits[i].split(")")[0]   #Making a dictionary with every pair
    BBB = all_orbits[i].split(")")[1] 

    pairs[BBB[0:len(BBB)-1]] = AAA

def get_closest(dict):
    x_nodes = "YOU"
    y_nodes = "SAN"

    while x_nodes != "COM":
        while y_nodes != "COM":                 #finding the intersection and adding distances for the planets 
            if dict[x_nodes] == dict[y_nodes]:  #YOU and SAN orbit
                return ( orbits(dict, dict["YOU"], dict[x_nodes]) + orbits(dict, dict["SAN"], dict[x_nodes]) ) 

            y_nodes = dict[y_nodes]         
        y_nodes = "SAN"
        x_nodes = dict[x_nodes]
    
print(get_closest(pairs))
f.close()
