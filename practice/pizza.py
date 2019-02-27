import numpy as np
import sys
import os
filename = sys.argv[1]
pizzaMat = []
f = open(filename,"r")
#first row
vals = str.split(f.readline().strip()," ")
R = int(vals[0])
C = int(vals[1])
L = int(vals[2])
H = int(vals[3])
print(vals)
print(L)
print(H)
for x in f:
    line = list(x.strip())
    pizzaMat.append(line)
print(pizzaMat)
pizza = np.array(pizzaMat)
print(pizza.transpose())
results = []
slices = 0
endI = 0
endJ = 0
while(endI != intR - 1):
    print()
#return coordinates of slice
def getRowSlice(pizza,startI,startJ):
    sliceCount = 0
    tomatoCount = 0
    mushroomCount = 0
    for i in range(startI,len(pizza)):
        for j in range(startJ,len(pizza[0])):
            sliceCount += 1
            if(pizza[i][j] == 'T'):
                tomatoCount += 1
            if(pizza[i][j] == 'M'):
                mushroomCount += 1
            if(sliceCount > H and (tomatoCount < L or mushroomCount < L)):
                return None
            if(tomatoCount >= L and mushroomCount >= L):
                if(sliceCount == H):
                    return i,j
def getColSlice(pizza,startI,startJ):
    i,j = getRowSlice(pizza.transpose(),startJ,startI)
    return j,i
