import codecs

def check_safe(nums):
    last_n = int(nums[0])
    pos = 0
    for n in nums[1:]:
        int_n = int(n)
        if(abs(last_n - int_n) > 3 or last_n == int_n):
            return False

        if(pos == 0):
            pos = -1 if last_n > int_n else 1
        else:
            if(int_n > last_n and pos == -1):
                return False
            if(int_n < last_n and pos == 1):
                return False
        
        last_n = int_n

    return True


def check_new_safe(nums):
    for n in range(0, len(nums)):
        new_nums = nums.copy()
        new_nums.pop(n)
        check = check_safe(new_nums)
        if(check):
            return True


safe = 0
new_safe = 0

with codecs.open('2.txt', encoding = 'utf-16') as f:
    for line in f:
        nums = line.split()
        check = check_safe(nums)
        if(check):
            safe = safe + 1
        elif(check_new_safe(nums)):
            new_safe = new_safe + 1

print(safe)
print(new_safe + safe)
