
from collections import defaultdict, deque
from methods import  read_data


data = read_data('testdata16.txt')
# data = read_data('fulldata16.txt')

class Valve:
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = int(rate)
        self.tunnelNames = tunnels
        self.maxVisits = len(tunnels) 
        self.travels = defaultdict()
        self.index = 0
    
    def print(self):
        print(self.name, str(self.rate), self.travels)

def GetValve(name, vs):
    return [v for v in vs if v.name == name][0]

def sortTunnel(x, y):
    return y.rate - x.rate

valvesOriginal = []

totalTravels = defaultdict(int)
    
for line in data:
    name = line.split(' ')[1]
    rate = line.split('=')[1].split(';')[0]

    if('valves' in line):
        tunnels = line.split('to valves ')[1].split(', ')
    else:
        tunnels = [line.split('to valve ')[1]]

    v = Valve(name, rate, tunnels)
    valvesOriginal.append(v)


def getNonZeroTunnels(original, current, travel):
    temp = defaultdict(int)
    nextTunnel = GetValve(current, valvesOriginal)
    totalTravels[(original, current)] = travel
    if(nextTunnel.rate > 0):
        if(temp[current] ==0 or temp[current] > travel):
            temp[current] = int(travel)
    else:
        for i in nextTunnel.tunnelNames:
            if(i != original and 
            (totalTravels[(original, i)] ==0 or totalTravels[(original, i)]  > travel + 1)):
                temp.update(getNonZeroTunnels(original, i, travel + 1))
    
    return temp


def loopForValve(v):
    temp = defaultdict(int)
    for t in v.tunnelNames:
        temp.update(getNonZeroTunnels(v.name, t, 1))

    v.travels = temp
    v.print()


valves = [v for v in valvesOriginal if v.rate > 0]

for i, v in enumerate(valves):
    loopForValve(v)
    v.index = i + 1


# Add AA back to the list since it's the starting point
start = GetValve('AA', valvesOriginal)
start.index = 0
loopForValve(start)
valves.append(start)

def updateState(state, index):
    stateList = list(state)
    stateList[index] = '1'
    return ''.join(stateList)

def bfs(starter, maxReleased):
    
    totalWithRate = len(valves)
    queueue = deque()

    state =  '1'
    for i in range(totalWithRate - 1):
        state += '0'

    allStates = defaultdict(lambda: -1)

    queueue.append((starter.name, 1, 0, starter.name, defaultdict(int), state))

    while queueue:
        currentName, minute, released, path, visits, state = queueue.popleft()

        visits[currentName] += 1
        current = GetValve(currentName, valves)

        print(currentName, released, path)
        print(state, allStates[state])

        if(minute >= 30
            or state.count('1') >= totalWithRate
            # or (allStates[state] >= released and released > 0)
            or current.maxVisits < visits[currentName]
            or (len(path) > 9 and released == 0)):
            continue

        # print(state, allStates[state])

        allStates[state] = released

        for tname, ttime in current.travels.items():
            newminute = minute + ttime
            tValve =  GetValve(tname, valves)
            maximumVisits = tValve.maxVisits
            newState = updateState(state, tValve.index)
            if(newminute < 30 and visits[tname] <= maximumVisits and allStates[newState] < released):
                print('going to', tname, newState)
                queueue.append((tname, newminute, released, path + " " + tname, visits.copy(), state))

        if(state[current.index] != '1' and currentName != 'AA'):
            print('opening', currentName)
            #open
            released  += (30 - minute) * current.rate 
            state = updateState(state, current.index)
            path = path + " open " + currentName
            minute += 1
            allStates[state] = released

            for tname, ttime in current.travels.items():
                newminute = minute + ttime
                tValve =  GetValve(tname, valves)
                maximumVisits = tValve.maxVisits
                newState = updateState(state, tValve.index)
                if(newminute < 30 and visits[tname] <= maximumVisits  and allStates[newState] < released):
                    print('going to', tname, newState)
                    queueue.append((tname, newminute, released, path + " " + tname, visits.copy(), state))

        print()
        # print(path + ' ' + str(released))
        maxReleased = max(maxReleased, released)
    
    return (maxReleased, minute)


print()
print('part 1')
print(bfs(start, 0))

