#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # 비트연산문제
    result = 0
    for i in a:
        result = result ^ i
    print(result)
    return result
    #두번 나온다는건 xor 연산을 두번하면 해당 비트는 모두 0이 된다는 뜻이다.
    #그럼 단 하나뿐인 값의 비트가 1이 되므로, 굳이 다시 검사할 필요없이 그 값을 리턴하면 된다.
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

   # fptr.write(str(result) + '\n')

    #fptr.close()
