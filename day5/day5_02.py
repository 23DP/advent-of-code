f = open(path)

if f.mode == "r":
	r = f.read()

puzzle_input = r.split(",")
parsed = list(map(int, puzzle_input))

i = 0
while i < len(parsed):
    instruction = parsed[i]
    operation = instruction%100 

    if operation == 99:
        break
    elif (operation == 1) | (operation == 2):

        rm = (instruction%1000 - instruction%100)/100 
        lm = (instruction%10000 - instruction%1000)/1000 
        dest = parsed[i+3] #always in position mode

        right_op = parsed[ i+1 ] if ( rm == 1) else parsed[ parsed[i + 1] ]
        left_op = parsed[ i+2 ] if ( lm ==1) else parsed[ parsed[i + 2] ]

        parsed[dest] = (left_op + right_op) if (operation == 1) else (left_op*right_op)
        i += 4

    elif operation == 3:
        dest = parsed[ i+1 ]
        parsed[dest] = 5
        i += 2
    elif operation == 4:
        dest = parsed[ i+1 ]
        print(i, ": ", parsed[dest])
        i += 2

    elif operation == 5:

        fm = (instruction%1000 - instruction%100)/100       #mode for the first operand
        sm = (instruction%10000 - instruction%1000)/1000    #mode for the second operand
        nz =  parsed[ i+1 ] if ( fm == 1) else parsed[ parsed[i + 1] ]
        if nz != 0:
            i = parsed[ i+2 ] if ( sm == 1) else parsed[ parsed[i + 2] ]
        else:
            i += 3

    elif operation == 6:

        fm = (instruction%1000 - instruction%100)/100 
        sm = (instruction%10000 - instruction%1000)/1000 
        nz =  parsed[ i+1 ] if ( fm == 1) else parsed[ parsed[i + 1] ]
        if nz == 0:
            i = parsed[ i+2 ] if ( sm ==1) else parsed[ parsed[i + 2] ]
        else:
            i += 3

    elif  operation == 7:

        fm = (instruction%1000 - instruction%100)/100     #mode for the left operand
        sm = (instruction%10000 - instruction%1000)/1000  #mode for the right operand
        dest = parsed[i+3] #always in position mode

        first_op = parsed[ i+1 ] if ( fm == 1) else parsed[ parsed[i + 1] ]
        second_op = parsed[ i+2 ] if ( sm ==1) else parsed[ parsed[i + 2] ]
        dest = parsed[i+3]

        parsed[dest] = 1 if (first_op < second_op) else 0
        i += 4

    elif operation == 8:

        fm = (instruction%1000 - instruction%100)/100      #mode for the left operand
        sm = (instruction%10000 - instruction%1000)/1000   #mode for the right operand
        dest = parsed[i+3] #always in position mode

        first_op = parsed[ i+1 ] if ( fm == 1) else parsed[ parsed[i + 1] ]
        second_op = parsed[ i+2 ] if ( sm ==1) else parsed[ parsed[i + 2] ]
        dest = parsed[i+3]

        parsed[dest] = 1 if (second_op == first_op) else 0
        i += 4

