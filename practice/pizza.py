import numpy as np
import sys
import os
#return coordinates of slice
def getRowSlice(pizza,startI,startJ):
    sliceCount = 0
    tomatoCount = 0
    mushroomCount = 0
    a = -1
    b = -1
    for i in range(startI,len(pizza)):
        for j in range(startJ,len(pizza[0])):
            sliceCount += 1
            if(pizza[i][j] == 'T'):
                tomatoCount += 1
            if(pizza[i][j] == 'M'):
                mushroomCount += 1
            if(sliceCount > H and (tomatoCount < L or mushroomCount < L)):
                return -1,-1
            if(tomatoCount >= L and mushroomCount >= L):
                if(sliceCount == H):
                    return i,j
    return -1,-1
def getColSlice(pizza,startI,startJ):
    i,j = getRowSlice(pizza.transpose(),startJ,startI)
    return j,i
filename = sys.argv[1]
pizzaMat = []
f = open(filename,"r")
#first row
vals = str.split(f.readline().strip()," ")
R = int(vals[0])
C = int(vals[1])
L = int(vals[2])
H = int(vals[3])
# print(vals)
# print(L)
# print(H)
for x in f:
    line = list(x.strip())
    pizzaMat.append(line)
#print(pizzaMat)
pizza = np.array(pizzaMat)
# print(pizza.transpose())
results = []
slices = 0
i = 0
j = 0
# print("R = " + str(R))
# print("C = " + str(C))
while(i < R  or j < C):
    # print("i = " + str(i))
    # print("j = " + str(j))
    rowI,rowJ = getRowSlice(pizza,i,j)
    colI,colJ = getColSlice(pizza,i,j)
    # print("rowI = " + str(rowI))
    # print("rowJ = " + str(rowJ))
    # print("colI = " + str(colI))
    # print("colJ = " + str(colJ))
    if(colI != -1):
        #found valid row slice
    #    print()
        result = [i,j,colI,colJ]
        results.append(result)
        j = colJ + 1
        slices += 1
    elif(rowI != -1):
        result = [i,j,rowI,rowJ]
        results.append(result)
        i = rowI + 1
        slices += 1
    else:
        #skip the cell ?
        i += 1
        j += 1
f = open("outputC.txt","w+")
f.write(str(slices) + "\n")
for result in results:
    f.write("%d %d %d %d\n"%(result[0],result[1],result[2],result[3]))
print(results)
