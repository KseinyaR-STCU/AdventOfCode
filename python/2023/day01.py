digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
words = ['one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = []

from functools import cmp_to_key

def sortPacket(x, y):
    return x[1] - y[1]

def grabFirstNumber(line):
    for iterator, char in enumerate(line):
        if(char in digits):
            return (int(char), iterator)
    return (0, -1)


def grabFirstWord(line):
    allWords = []

    for iterator, word in enumerate(words):
        allWords.append((int(digits[iterator]), line.find(word)))

    foundWords = [v for v in allWords if v[1] > -1]
    sortz = sorted(foundWords, key=cmp_to_key(sortPacket))
    
    if(len(sortz) > 0):
        return sortz[0]
    else:
        return ('zero', -1)


def grabLastWord(line):
    allWords = []

    for iterator, word in enumerate(words):
        allWords.append((int(digits[iterator]), line[::-1].find(word[::-1])))

    foundWords = [v for v in allWords if v[1] > -1]
    sortz = sorted(foundWords, key=cmp_to_key(sortPacket))
    
    if(len(sortz) > 0):
        return sortz[0]
    else:
        return ('zero', -1)


def getActualFirst(line):
    firstNums = grabFirstNumber(line)
    firstWords = grabFirstWord(line)

    allFirsts = [firstNums, firstWords]
    validFirsts = [v for v in allFirsts if v[1] > -1]
    sortedFirsts = sorted(validFirsts, key=cmp_to_key(sortPacket))

    return sortedFirsts[0]


def grabLastNumber(line):
    for iterator, char in enumerate(line[::-1]):
        if(char in digits):
            return (int(char), iterator)
    return (0, -1)


def getActualLast(line):
    lastNums = grabLastNumber(line)
    lastWords = grabLastWord(line)

    allLasts = [lastNums, lastWords]

    validLasts = [v for v in allLasts if v[1] > -1]
    sortedLasts = sorted(validLasts, key=cmp_to_key(sortPacket))

    return sortedLasts[0]


with open('full.txt') as f:
    for line in f:
        actualFirst = getActualFirst(line)
        actualLast = getActualLast(line)
       
        numbers.append((actualFirst[0] * 10) + actualLast[0])

print(sum(numbers))