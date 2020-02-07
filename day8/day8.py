import numpy as np
with open('input.txt', 'r') as f:
    input = f.read()
row, column = 25, 6 # given image dimensions
d3 = int(len(input)/(row*column)) # number of layers (dimension3)
image = np.empty([d3, row, column]) # creating empty picture

# get the count of occurrences of number in matrix
def getCount( matrix, number ): 
    count = 0
    for row in matrix:
        for elem in row:
            if elem == number:
                count+=1
    return count

# get the dimension(layer) with least zeroes           
def getDimension( nDimMatrix ):
    nth_dim, _, _ = nDimMatrix.shape
    best, retVal = np.Inf, 0 # inf to enter the first condition

    for i in range(0, nth_dim):
        zeroes = getCount(nDimMatrix[i], 0)
        if zeroes < best:
            best, retVal = zeroes, i
            
    return retVal
            
m=0
for i in range(d3): 
    for k in range(row):
        for j in range(column):
            image[i][k][j] = int(input[m])
            m+=1

layer = getDimension(image)
print( getCount(image[layer], 2)*getCount(image[layer], 1) )
