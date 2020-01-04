f = open(path)

if f.mode == "r":
	r = f.read()

puzzle_input = r.split(",")
parsed = list(map(int, puzzle_input))

i = 0
while i < len(parsed):
    instruction = parsed[i]
    operation = instruction%100   #last two digits
		
    if operation == 99:
        break
    elif (operation == 1) | (operation == 2):
        rm = int( (instruction%1000 - instruction%100)/100 )     #mode for the right operand
        lm = int( (instruction%10000 - instruction%1000)/1000 )  #mode for the left operand
        dest = parsed[i+3] #always in position mode
				
        right_op = parsed[ i+1 ] if ( rm == 1) else parsed[ parsed[i + 1] ]
        left_op = parsed[ i+2 ] if ( lm ==1) else parsed[ parsed[i + 2] ]
				
        parsed[dest] = (left_op + right_op) if (operation == 1) else (left_op*right_op)
        i += 4
    elif operation == 3:
        dest = parsed[ i+1 ]
        parsed[dest] = 1    #only one input..
        i += 2
    else :
        dest = parsed[i + 1]  
        print(i, ": ", parsed[dest])
        i += 2
