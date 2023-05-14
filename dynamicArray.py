import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def query1(x, last_answer, n):
    idx = ((x^last_answer) %n)
    return idx

def query2(arr, x, y, last_answer, n):
    idx = query1(x, last_answer, n)
    return arr[idx][y % len(arr[idx])]

def dynamicArray(n, queries):
    # Write your code here
    array_2d=[[]]
    answers = []
    last_answer = 0
    
    for query in queries:
        x = query[1]
        y = query[2]
        if query[0] == 1: 
            # query 1
            idx = query1(x, last_answer, n)
            while len(array_2d) < idx + 1:
                 array_2d.append([])
            array_2d[idx].append(y)
        else: #query 2
            last_answer = query2(array_2d, x, y, last_answer, n)
            answers.append(last_answer)
  #  print(answers)
    return answers

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
