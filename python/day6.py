
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()


def get(count):
    marker = []

    for line in data:
        for iterator, character in enumerate(line):
            marker.append(character)
            if (len(marker) == count + 1):
                marker = marker[1:]
            
            if(len(marker) == count and len(set(marker)) == count):
                return (iterator + 1)
        

print(get(4))
print(get(14))