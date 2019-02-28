import numpy as np
import sys
from slide import Slide

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
    i = 0
    slides = []
    #get list of slides
    while(i < len(tags)):
        orientation = tags[i][0]
        if(orientation == 'H'):
            slide = Slide(tags[i],i)
        else:
            photo1 = tags[i]
            photo2 = tags[i+1]
            slide = Slide(photo1,i,photo2,i+1)
            i += 1
        slides.append(slide)
        i += 1
