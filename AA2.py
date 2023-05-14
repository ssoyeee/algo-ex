import sys

sys.stdin=open("input.txt","r")
def DFS(x):
    if x==0:
        return #함수를 종료시켜라 
    else:
        DFS(x//2)
        print(x%2, end=' ') #stack 처리

if __name__=="__main__":
    n=int(input())
    DFS(n)