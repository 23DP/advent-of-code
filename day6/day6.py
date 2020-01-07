f = open(path, "r")

if f.mode == "r":
	all_orbits = f.readlines()

pairs = {}
connections = 0

def orbits(dict, key):
    AAA = dict[key]
    cnt = 1   #Starting from 1 because they all orbir around COM

    while AAA != "COM":     #count how many pairs is key from COM
        cnt += 1
        BBB = AAA
        AAA = dict[BBB]

    return cnt


# COM ) AAA ) BBB
for i in range(len(all_orbits)):
    AAA, BBB = all_orbits[i].split(")")   #Making a dictionary with every pair

    pairs[BBB[0:len(BBB)-1]] = AAA



for node in pairs.keys():
    connections += orbits(pairs, node)  #sum the count for every node in our system
    
print(connections)
    
