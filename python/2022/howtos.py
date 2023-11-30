# HOW TO SORT BY A PROPERTY
# from functools import cmp_to_key

# def sortPacket(x, y):
#     return x.property - y.property

# sortz = sorted(listName, key=cmp_to_key(sortPacket))


# HOW TO FILTER A LIST
# [v for v in visits if v == 1] (or whatever condition) 

# HOW TO GET ONE PROPERTY FROM A LIST
# props = list(map(lambda n: n.propertyName, listName))


# HOW TO EVAL A FILE
# import ast
# ast.literal_eval()

# HOW TO FIND AN ITEM IN A LIST BY A PROPERTY (id here)
# def findItemIndexById(list, id):
#     matchCave = [x for x in list if x.id == id][0]
#     return list.index(matchCave)

# QUEUES and DICTs 
# from collections import dict, defaultdict, deque