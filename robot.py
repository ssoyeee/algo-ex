from shutil import move
import sys
import os
from tkinter import Y

# Python program to check if the given path for a robot is circular
# or not
N = 0
E = 1
S = 2
W = 3
 
# This function returns true if the given path is circular,
# else false
def isCircular(_commands):
 
    # Initialize starting point for robot as (0, 0) and starting
    # direction as N North
    x = 0
    y = 0
    dir = N
 
    # Traverse the path given for robot
    for i in range(len(_commands)):
    
        # Find current move
        move = _commands[i]
    
        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1)%4
        elif move == 'L':
            dir = (4 + dir - 1)%4
            # If move is Go, then change x or y according to
            # current direction
        else:    # if move == 'G'
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            else:
                x -= 1
        return (x,y)             
    
    
    if isCircular == (0,0): 
        print("YES") 
    else: 
        print("NO")

# if isCircular(path):
#     print("YES")
# else:
#     print("NO")

if __name__ =='__main__':
    os.environ['OUTPUT_PATH'] = 'input.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
        

    _commands_cnt = 0
    _commands_cnt = int(input().strip())
    _commands_i=0
    _commands = []
    while _commands_i < _commands_cnt:
        _commands_item = sys.stdin.readline()
        _commands.append(_commands_item)
        _commands_i+=1
        
    # if isCircular == (0,0): 
    #     print("YES") 
    # else: 
    #     print("NO")

    res = isCircular(_commands)
    # print(res is None)
    
    for res_cur in res:
        # print(str(res_cur))
        fptr.write(str(res_cur))
    
    


    fptr.close()