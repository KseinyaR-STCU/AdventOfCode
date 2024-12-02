import codecs

left = []
right = []

with codecs.open('1.txt', encoding = 'utf-16') as f:
    for line in f:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))


left.sort()
right.sort()

dist = 0

for i in range(0, len(left)):
    dist = dist + abs(left[i] - right[i])

print("part 1")
print(dist)

sim = 0

for i in range(0, len(left)):
    sim = sim + (left[i] * sum(x == left[i] for x in right))

print("part 2")
print(sim)