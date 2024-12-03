from methods import read_data, read_udf_data, splitWholeGrid

data = read_data('in.tst')
data = read_udf_data('in.txt')

grid = splitWholeGrid(data)

maxX = len(grid[0])
maxY = len(grid)

def xSlope(step):
    trees = 0
    currX = 0

    for i in range(1, maxY):
        currX += step
        currX = (currX % maxX)
        if(grid[i][currX] == '#'):
            trees += 1 
    
    return trees

def ySlope():
    trees = 0
    currX = 0

    for i in range(2, maxY, 2):
        currX += 1
        currX = (currX % maxX)
        if(grid[i][currX] == '#'):
            trees += 1
    
    return trees

print("part 1")
print(xSlope(3))

print("part 2")
print(xSlope(1) * xSlope(3) * xSlope(5) * xSlope(7) * ySlope())