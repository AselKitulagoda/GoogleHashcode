class Slide:
    def __init__(self,photo1,photo2 = [],tags = [],ids = []):
        id_1 = int(photo1[1])
        ids.append(id_1)
        tag_1 = []
        tag_2 = []
        #get tags of first pic
        for i in range(2,len(photo1)):
            tag_1.append(photo1[i])
        if(len(photo2) != 0):
            id_2 = int(photo2[1])
            ids.append(id_2)
            #get tags of 2nd pic
            for i in range(2,len(photo2)):
                tag_2.append(photo1[i])
        #union of 2 tag lists
        self.tags = list(set.union(tag_1,tag_2))
        self.ids = ids
    
    def _str_(self):
        str1 = "tags = " + str(self.tags) + "/n"
        str2 = "ids = " + str(self.ids)
        return (str1 + str2)

