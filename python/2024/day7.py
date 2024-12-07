from methods import  read_data, read_udf_data, splitNumsOnWhitespace
import math
import collections
import time

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')


class Equation:
    def __init__(self, total, opts):
        self.total = int(total)
        self.opts = list(map(lambda n: int(n), opts.split()))
    
    def print(self):
        print(self.total, self.opts)


equations = []

for line in data:
    parts = line.split(':')
    equations.append(Equation(parts[0], parts[1]))

valids = []

def maths(current, expected, nums):
    next_num = nums[0]
    plus = current + next_num
    times = current * next_num
    concat = int( str(current) + str(next_num))

    # if(plus > expected and times > expected):
    #     return 0

    plus_response = 0
    times_response = 0
    concat_response = 0

    if(len(nums) == 1):
        if(plus == expected or times == expected or concat == expected):
            return expected
        else:
            return 0
    else:
        # if(plus < expected):
        #     plus_response = maths(plus, expected, nums[1:])
        
        # if(plus_response > 0):
        #     return plus_response
        
        # if(plus_response == 0 and times < expected):
        #     times_response = maths(times, expected, nums[1:])

        plus_response = maths(plus, expected, nums[1:])
        times_response = maths(times, expected, nums[1:])
        concat_response = maths(concat, expected, nums[1:])
        return max(plus_response, times_response, concat_response)
    
    return 0


def should_skip(equation):
    if(1 in equation.opts):
        return False
    return sum(equation.opts) > equation.total or math.prod(equation.opts) < equation.total

def easy_add(equation):
    if(sum(equation.opts) == equation.total or math.prod(equation.opts) == equation.total):
        return True
    else:
        return False


p1 = 0

for e in equations:
    # if(not should_skip(e)):
    #     if(easy_add(e)):
    #         p1 += e.total
    #         goochies.append(e.total)
    #         print('yipee')
    #         e.print()
    #     else:
    answer = maths(e.opts[0], e.total, e.opts[1:])
    if(answer > 0):
        p1 += answer
    # else:
    #     print('skipeed')
    #     e.print()

print(p1)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# print(goochies)

# print("part 2")
# print(p2)