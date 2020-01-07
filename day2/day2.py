f = open(path, "r")

if f.mode == "r":
	r = f.read()

puzzle_input = r.split(",")
parsed = list(map(int, puzzle_input))

'''
parsed[1] = 12
parsed[2] = 2
'''

def get_first(input: list) -> int:

    for i in range(0, len(input), 4):
        if input[i] == 99:
            break
        else:
            operation = input[i]
            left_op = input[ input[i+1] ]
            right_op = input[ input[i+2] ]
            dest = input[i+3]

            input[dest] = (left_op + right_op) if (operation == 1) else (left_op*right_op)
    return input[0]


print(get_first(parsed))
            
f.close()
