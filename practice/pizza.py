import numpy as np
import sys
import os
filename = sys.argv[1]
pizzaMat = []
f = open(filename,"r")
#first row
vals = str.split(f.readline().strip()," ")
L = vals[2]
H = vals[3]
print(vals)
print(L)
print(H)
for x in f:
    line = list(x.strip())
    pizzaMat.append(line)
print(pizzaMat)
