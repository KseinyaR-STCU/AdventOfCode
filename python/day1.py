current = 0
largest = 0

with open('fulldata.txt') as f:
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

with open('fulldata.txt') as f:
    for line in f:
        if line.rstrip():
            current = current + int(line.rstrip())
        else:
            sums.append(current)
            current = 0

sums.sort(reverse=True)

print(sum(sums[0:3]))
