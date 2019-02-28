class Slide:
    def __init__(self,photo1,id_1,photo2 = [],id_2 = -1,tags = [],ids = []):
        ids = [id_1]
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
                tag_2.append(photo2[i])
        #union of 2 tag lists
        self.tags = list(set.union(set(tag_1),set(tag_2)))
        self.ids = ids 
    def __str__(self):
        str1 = "tags = " + str(self.tags) + " "
        str2 = "ids = " + str(self.ids) + "\n"
        return (str1 + str2)

