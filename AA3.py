import sys 
sys.stdin=open("input.txt","r")
def DFS(L, sum): #L: index number, level
    if sum>total//2:
        return
    if L == n: #level이 입력받은 원소의 개수n과 같으면
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")