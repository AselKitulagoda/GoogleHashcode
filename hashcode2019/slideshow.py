import numpy as np
import sys
import itertools 
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
        print(slide)
        i += 1
    dict_tags = {}
    for s in slides:
        tags = s.tags
        ids = s.ids
        key = ""
        for id in ids:
            key += str(id) + " "
        dict_tags[key] = set(tags)
    print(dict_tags)
    # for s in slides:
    #     tags = s.tags
    #     for tag in tags:
    #         for id_ in s.ids:
    #             prevIds = set([])
    #             if tag in dict_tags.keys():
    #                 prevIds = dict_tags[tag]
    #             dict_tags[tag] = prevIds | set([id_])
    # print(dict_tags)
    #new dictionary storing intersection
    intersections = {}
    for x,y in itertools.combinations(dict_tags,2):
        i_key = x + "->" + y
        i_common = dict_tags[x] & dict_tags[y]
        intersections[i_key] = i_common 
    print(intersections)


    differencesA = {}
    for x,y in itertools.combinations(dict_tags,2):
        d_key = x + "->" + y
        d_diff = dict_tags[x] - dict_tags[y]
        differencesA[d_key] = d_diff
    print(differencesA)

    differencesB = {}
    for x,y in itertools.combinations(dict_tags,2):
        d_key = y + "->" + x
        d_diff = dict_tags[y] - dict_tags[x]
        differencesB[d_key] = d_diff
    print(differencesB)

    interests = {}
    for x,y in itertools.combinations(dict_tags,2):
        i_key = x + "->" + y
        j_key = y + "->" + x
        sizeA = len(intersections[i_key])
        sizeB = len(differencesA[i_key])
        sizeC = len(differencesB[j_key])
        interest = np.amin([sizeA,sizeB,sizeC])
        interests[i_key] = interest
    print(interests)
        
