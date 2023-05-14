#재귀함수와 스택
import sys
sys.stdin=open("input.txt","r")
def DFS(v):
    if v>7:
        return
    else:
        print(v) #방문 
        DFS(v*2) #호출
        DFS(v*2+1) #호출
#----> 전위순회 
# DFS(v*2)
# DFS(v*2+1)
# print(v, end=" ") -방문
#  -----> 후위순회
if __name__=="__main__":
 
    DFS(1)