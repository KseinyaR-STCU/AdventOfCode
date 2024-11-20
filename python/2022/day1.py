import codecs

current = 0
largest = 0

with codecs.open('1.txt', encoding = 'utf-16') as f:
    for line in f:
        if line.rstrip():
            current = current + int(line.rstrip())
        else:
            if current > largest:
                largest = current
            current = 0

print(largest)


current = 0
sums = []

with codecs.open('1.txt', encoding = 'utf-16') as f:
    for line in f:
        if line.rstrip():
            current = current + int(line.rstrip())
        else:
            sums.append(current)
            current = 0

sums.sort(reverse=True)

print(sum(sums[0:3]))
