# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys
from collections import deque


def QueueTwoStacks(operations):
    q = deque([]) #빈스트링 ([''])
    res = []
    
    for opr in operations :
        if opr[0] == '1':
            value = opr.split()[-1]
            q.append(value)
        elif opr[0] == '2':
            q.popleft()
        elif opr[0] == '3':
            res.append(q[0]) # 큐에 들어있는 값을 넘겨야함
    return res

if __name__ =='__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ops = []
    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

# 42 (-42) 14 (print 14) 28 (print 14 28) 60 78 (-14) (-28) (print 60 78)

    results = QueueTwoStacks(ops)
    print(results)
    # fptr.write('\n'.join(map(str, results)))
    # fptr.write('\n')

    # fptr.close()
