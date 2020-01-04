f = open(path)

if f.mode == "r":
	all_orbits = f.readlines()

pairs = {}
connections = 0

def orbits(dict, key):
    AAA = dict[key]
    cnt = 1   #Starting from 1 because they all orbit around COM

    while AAA != "COM":     #count how many pairs is key from COM
        cnt += 1
        BBB = AAA
        AAA = dict[BBB]

    return cnt


# COM ) AAA ) BBB
for i in range(len(all_orbits)):
    AAA = all_orbits[i].split(")")[0]   #Making a dictionary with every pair
    BBB = all_orbits[i].split(")")[1] 

    pairs[BBB] = AAA


for node in pairs.keys():
    connections += orbits(pairs, node)  #sum the count for every node in our system
    
print(connections)
    
