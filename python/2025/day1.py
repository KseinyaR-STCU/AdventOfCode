import codecs

count = 50
zeros = 0
all_zeros = 0
 
with codecs.open('in.txt', encoding = 'utf') as f:
    for line in f:
        dir = line[0]
        num = int(line[1:])

        modded = num % 100

        if (num / 100) >= 1:
            all_zeros = all_zeros + int(num / 100)

        if dir == 'L':
            if (modded > count and count != 0):
                all_zeros = all_zeros + 1

            count = count - (modded)
            if count < 0:
                count = 100 + count
        else:
            if (modded > 100 - count):
                all_zeros = all_zeros + 1

            count = count + (modded)
            if count > 99:
                count = count - 100
        
        if count == 0:
            zeros = zeros + 1



print("part 1")
print(zeros)

print("part 2")
print(all_zeros + zeros)
