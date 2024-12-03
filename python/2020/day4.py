from methods import read_data, read_udf_data, splitNumsOnSeparator

data = read_data('in.tst')
data = read_udf_data('in.txt')

p1 = 0
p2 = 0

keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

current_pass = set()
current_pass_p2 = set()

def check_valid(key, value):
    if(key == 'cid'): 
        return False
    elif(key == 'byr' and int(value) >= 1920 and int(value) <= 2002):
        return True
    elif(key == 'iyr' and int(value) >= 2010 and int(value) <= 2020):
        return True
    elif(key == 'eyr' and int(value) >= 2020 and int(value) <= 2030):
        return True
    elif(key == 'hgt' and ((value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193) or (value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76))):
        return True
    elif(key == 'hcl' and value[0] == '#' and len(value) == 7):
        return True
    elif(key == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return True
    elif(key == 'pid' and value.isnumeric() and len(value) == 9):
        return True
    
    return False


for line in data:
    if(not line.strip()):
        # print('new passport')
        # print(current_pass)
        if(keys == current_pass):
            p1 += 1
        current_pass = set()

        if(keys == current_pass_p2):
            p2 += 1
        current_pass_p2 = set()
    else:
        sections = line.split()
        for section in sections:
            s = section.split(':')
            key, value = s[0], s[1]
            if(key != 'cid'):
                current_pass.add(key)
            if(check_valid(key, value)):
                current_pass_p2.add(key)

# print('new passport')
# print(current_pass)
if(keys == current_pass):
    p1 += 1

if(keys == current_pass_p2):
    p2 += 1

print("part 1")
print(p1)

print("part 2")
print(p2)