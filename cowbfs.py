from operator import ne
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

MAX=10000
ch = [0] * (MAX+1) #visited (index starts from 0 so need to add 1 to MAX size)
dis = [0] * (MAX+1) #distance list

n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m: #m is destination
        break
    for next in(now-1, now+1, now+5): # will explore each tuples 3times
        if 0<next<=MAX:
            if ch[next]==0: # need to visit if it is not visited
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1 #0 1 2 in dis list
print(dis[m])