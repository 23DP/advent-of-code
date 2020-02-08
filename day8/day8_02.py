import numpy as np
with open('input.txt', 'r') as f:
    input = f.read()
row, column =  6,25 #given image dimensions
d3 = int(len(input)/(row*column)) # number of layers (dimension3)
image = np.empty([d3, row, column]) # creating empty picture
          
m=0
for i in range(d3):
    for j in range(row):
        for k in range(column):
            image[i][j][k] = int(input[m])
            m+=1


finalPic = image[0] #initializing the picture with the first layer
for layer in image:
    for i in range(0, row):
        for j in range(0, column):
            if finalPic[i][j] == 2:          #if the value of the pixel is 2, meaning transparent,
                finalPic[i][j] = layer[i][j] #change it's value to the corresponding pixel in the current layer

for a in range(0, row):
    for b in range(0, column):
        print(' ' if finalPic[a][b] == 0 else '•', end = '')
    print('')
