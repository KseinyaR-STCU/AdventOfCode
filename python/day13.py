
def read_data():
    fileName = 'testdata.txt'
    # fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

bads = set()
goods = set()

currentRow = 0

# parsing attempt fail
# def getPacket(line):
#     inList = 0
#     current = ''
#     currentz = []
#     list = []

#     for i, x in enumerate(line):
#         if(i == 0):
#             continue

#         if(x == '['):
#             if(current != ''):
#                 currentz.append(current)
            
#             if(len(currentz) > 0):
#                 list.append((currentz, inList))
#             currentz = []
#             current = ''
#             inList += 1
#         elif(x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
#             current += x
#         elif(x == ','):
#             if(current != ''):
#                 currentz.append(current)

#             # if(inList == 0 and len(currentz) > 0):
#             #     list.append((currentz, inList + 1))
#             #     currentz = []

#             current = ''
#         elif(x == ']'):
#             if(current != ''):
#                 currentz.append(current)
            
#             if(len(currentz) > 0):
#                 list.append((currentz, inList))
#             currentz = []
#             current = ''
#             inList -= 1
    
#     return list


def compareInts(left, right):
    if(int(left) < int(right)):
        return True
    elif(int(left) > int(right)):
         return False
    else:
        return None

def compare(l, r):
    if (type(l) == list and type(r) == list):
        return compareLists(l, r)
    elif(type(l) == int and type(r) == int):
        return compareInts(l, r)
    elif(type(l) == list and type(r) == int):
        return compareLists(l, [r])
    else:
        return compareLists([l], r)

def compareLists(left, right):
    ri = 0

    for i, l in enumerate(left):
        if(len(right) -1 < i):
            bads.add(index)
            return False

        r = right[ri]
        check = compare(l, r)
        
        if(check == True):
            goods.add(index)
            return True
        elif(check == False):
            bads.add(index)
            return False
        elif(check == None):
            ri += 1
    
    if(len(right) >= len(left) and index not in bads):
        goods.add(index)
        return True
    
    return None


index = 1
totals = 1

for line in data:
    if(line == ''):
        currentRow = 0
        index += 1
        totals += 1
        continue

    if(currentRow == 0):
        # left = getPacket(line)
        left = eval(line)
        currentRow += 1
        continue
    elif(currentRow == 1):
        # right = getPacket(line)
        right = eval(line)


    print(left)
    print(right)

    check = compareLists(left, right)
    if(check == True):
        goods.add(index)
    elif(check == False):
        bads.add(index)


print('part 1')
print(sum(goods))


# i gave up and sorted manually lol
# allPackets = []

# for line in data:
#     if(line == ''):
#         continue

#     allPackets.append(eval(line))

# allPackets.append([[2]])
# allPackets.append([[6]])

# allPackets.sort()

# print(allPackets)