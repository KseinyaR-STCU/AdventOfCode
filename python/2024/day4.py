from methods import  read_data, read_udf_data, splitNumsOnWhitespace

data = read_data('in.tst')
data = read_data('in.txt')

p1 = 0

grid = []
for line in data:
    grid.append(list(map(lambda n: n, line[::1])))


for g in grid:
    p1 += ''.join(g).count('XMAS')
    p1 += ''.join(g).count('SAMX')

flipped = list(zip(*grid))

for g in flipped:
    p1 += ''.join(g).count('XMAS')
    p1 += ''.join(g).count('SAMX')

print(p1)
maxI = len(grid)
maxJ = len(grid[0])

def check_dr(grid, i, j, char):
    count = 0
    if(i+1 < maxI and j+1 < maxJ and grid[i + 1][j +1] == char[0]):
        if(len(char) == 1):
            print(i+1, j+1)
            count += 1
        else:
            count += check_dr(grid, i + 1, j + 1, char[1:])
    return count


def check_dl(grid, i, j, char):
    count = 0
    if(i+1 < maxI and j-1 >= 0 and grid[i + 1][j -1] == char[0]):
        if(len(char) == 1):
            print(i+1, j-1)
            count += 1
        else:
            count += check_dl(grid, i + 1, j - 1, char[1:])
    return count


def check_ur(grid, i, j, char):
    count = 0
    if(i -1 >= 0 and j+1 < maxJ and grid[i - 1][j  + 1] == char[0]):
        if(len(char) == 1):
            print(i-1, j+1)
            count += 1
        else:
            count += check_ur(grid, i - 1, j + 1, char[1:])
    return count


def check_ul(grid, i, j, char):
    count = 0
    if(i -1 >= 0 and j-1 >= 0 and grid[i - 1][j -1] == char[0]):
        if(len(char) == 1):
            print(i-1, j-1)
            count += 1
        else:
            count += check_ul(grid, i - 1, j - 1, char[1:])
    return count


def check_all(grid, i, j, char):
    count = 0
    if(i+1 < maxI and j+1 < maxJ and grid[i + 1][j +1] == char[0]):
        count += check_dr(grid, i + 1, j + 1, char[1:])

    if(i+1 < maxI and j-1 >= 0 and grid[i + 1][j -1] == char[0]):
        count += check_dl(grid, i + 1, j - 1, char[1:])
    
    if(i -1 >= 0 and j-1 >= 0 and grid[i - 1][j -1] == char[0]):
        count += check_ul(grid, i - 1, j - 1, char[1:])

    if(i -1 >= 0 and j+1 < maxJ and grid[i - 1][j  + 1] == char[0]):
        count += check_ur(grid, i - 1, j + 1, char[1:])

    return count


# for i in range(0,len(grid)):
#     for j in range(0,len(grid[0])):
#         if (grid[i][j] == 'X'):
#             p1 += check_all(grid, i, j, 'MAS')


print('part 1')
print(p1)

p2 = 0

tester = 0

for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
        if (grid[i][j] == 'A'):
            
            tester += check_ul(grid, i, j, 'M')
            tester += check_ur(grid, i, j, 'M')
            tester += check_dl(grid, i, j, 'S')
            tester += check_dr(grid, i, j, 'S')

            if(tester == 4):
                p2 += 1
            
            tester = 0

            tester += check_ul(grid, i, j, 'M')
            tester += check_ur(grid, i, j, 'S')
            tester += check_dl(grid, i, j, 'M')
            tester += check_dr(grid, i, j, 'S')

            if(tester == 4):
                p2 += 1
            
            tester = 0

            tester += check_ul(grid, i, j, 'S')
            tester += check_ur(grid, i, j, 'S')
            tester += check_dl(grid, i, j, 'M')
            tester += check_dr(grid, i, j, 'M')

            if(tester == 4):
                p2 += 1
            
            tester = 0

            tester += check_ul(grid, i, j, 'S')
            tester += check_ur(grid, i, j, 'M')
            tester += check_dl(grid, i, j, 'S')
            tester += check_dr(grid, i, j, 'M')

            if(tester == 4):
                p2 += 1
            
            tester = 0

print('part 2')
print(p2)

