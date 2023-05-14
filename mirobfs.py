import sys 
from collections import deque

sys.stdin = open("input.txt","r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range (7)] #making maze
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0)) #starting point
board[0][0]=1 #if visited mark as 1
while Q: #if Q is false - break
    tmp = Q.popleft()
    for i in range(4): #in the next block we need to explore 4 directions
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i] # directions
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0: #if it is wall we cannot go
            board[x][y]=1 #make it as wall, checked
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

