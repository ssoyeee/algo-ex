from os import path
import sys 
sys.stdin=open("input.txt","r")
def DFS(v): #노드번호 v
    global cnt
    if v==n: #종착지점
        cnt+=1
        for x in path:
            print(x, end=' ')
        print() #줄바꿈
    else:
        for i in range(1, n+1): #n가지로 가지를 뻗음
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop() #뒤로 back했을 때는 pop해서 빼주기
                ch[i]=0 #check 풀어주기



if __name__=="__main__":
    n, m=map(int, input().split()) #n: node number, m: line nubmer
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1) #visited
    for i in range(m):
        a, b = map(int,input().split())
        g[a][b]=1 #방향그래프
        cnt = 0
        path=[]
        path.append(1)
        ch[1]=1 #방문했음
        DFS(1) #1번 노드로 넘어감
        print(cnt)