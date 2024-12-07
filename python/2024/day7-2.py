from methods import  read_data, read_udf_data, splitNumsOnWhitespace
import math
from collections import defaultdict, deque
from operator import add, mul
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



def queue_it_up(equation):
    expected_total = equation.total
    queueue = deque()
    queueue.append((equation.opts[0], equation.opts[1:]))

    while queueue:
        newest = queueue.popleft()
        current_amount = newest[0]
        more_nums = newest[1]
        the_rest = more_nums[1:]

        next_num = more_nums[0]
        plus = add(current_amount, next_num)
        times = mul(current_amount, next_num)
        concat = int( str(current_amount) + str(next_num))

        if(len(more_nums) <= 1):
            if(plus == expected_total or times == expected_total or concat == expected_total):
                # print(expected_total)
                return True
        else:
            #### WTF WOULD THESE CHECKS BREAK IT???
            # if(plus <= expected_total):
            #     queueue.append((plus, the_rest))
            # if(times <= expected_total):
            #     queueue.append((times, the_rest))
            
            queueue.append((plus, the_rest))
            queueue.append((times, the_rest))
            queueue.append((concat, the_rest))
    
    return False


p1 = 0

for e in equations:
    if(queue_it_up(e)):
        p1 = p1 + e.total


print(p1)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')