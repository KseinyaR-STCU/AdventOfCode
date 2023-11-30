
def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

cycle = 0
register = 1
cycles = [20, 60, 100, 140, 180, 220]
# cycles = list(range(20,220+1,40))
# cycles = [item for item in range(20, 220+1, 40)]

strengths = []
pixels = []

def checkCycle():
    drawPixel()

    for c in cycles:
        if(cycle == c):
            print('cycle ' + str(c))
            print(register)
            strengths.append(register * c)


def drawPixel():
    test = abs(register - ((cycle - 1) % 40))
    if(test < 2):
        pixels.append('#')
    else:
        pixels.append('.')



for line in data:
    if(line.startswith('noop')):
        cycle += 1
        checkCycle()
    else:
        value = int(line.split(' ')[1])
        cycle += 1
        checkCycle()
        cycle += 1
        checkCycle()

        if(cycle == 20): break
        
        register += value


print(sum(strengths))

start = 0
for c in cycles:
    print(str.join('', pixels[start:c + 19]))
    start = c + 20
