#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s.split(":") #hour : min : sec AM/PM

    if s[-2:] == "PM":
        if time[0] != '12':
            if int(time[0]) < 12:
                time[0] = str(int(time[0]) + 12)
        else:
            time = time[:]                
    elif s[-2:] == "AM": #if AM
        if time[0] == '12':
            time[0] = "00"
        else:
            time = time[:]

    ntime = ":".join(time)
    return ntime[:-2]
   
if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

 #   fptr.write(result + '\n')

  #  fptr.close()
