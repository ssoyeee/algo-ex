import sys
from collections import deque

sys.stdin=open("input.txt","r")

def DFS(L, sum, tsum): #L: a라는 list를 접근하는 index number, sum = 부분집합의 합
    global res
    if sum+(total-tsum)<res: #cutting edge
        return
    if sum>c:#cutting edge
        return
    if L==n:#부분집합이 하나가 완성되면
        if sum>res:
            res=sum
    else:
            DFS(L+1, sum+a[L], tsum+a[L]) #a list의 L번째 있는 원소를 부분집합에 참여시키겠다
            DFS(L+1, sum, tsum+a[L])

if __name__=="__main__":
    c, n = map(int, input().split()) #c: 트럭의 총무게, n:강아지 몇마리
    a=[0]*n #바둑이의 각각의 무게
    res =-2147000000 #최종적인 답을 저장할 변수, 가장 큰 값을 찾을 것이므로, 가장 작은 값으로 초기화
    for i in range(n):
        a[i] = int(input())
    total=sum(a)
    DFS(0,0,0)
    print(res)
