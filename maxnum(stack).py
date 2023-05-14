import sys
sys.stdin=open("input.txt","r")
num, m = map(int, input().split())
num = list(map(int, str(num))) #num이 하나의 정수인데 그 정수를 한자리씩 분리해야됨
# str으로 num을 변환한걸 int화되어 하나하나 매치 
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
# for x in stack:
#     print(x, end='')
print(res)
