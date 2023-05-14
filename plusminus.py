#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] == 0: #0보다 작은지 같은지 비교
            z = z+1
        elif arr[i] < 0:
            neg = neg+1
        else:
            pos = pos+1
            
    pos_frac = float(pos/len(arr))
    neg_frac = float(neg/len(arr))
    z_frac = float(z/len(arr))
    print(f'{pos_frac: 0.6f}')
    print(f'{neg_frac: 0.6f}')
    print(f'{z_frac: 0.6f}')
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
