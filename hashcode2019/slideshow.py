import numpy as np
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    tags = []
    f = open(filename,"r")

    #first row
    photoCount = int(f.readline())

    #rest
    for x in range(photoCount):
        line = str.split(f.readline().strip()," ")
        tags.append(line)
    f.close()
