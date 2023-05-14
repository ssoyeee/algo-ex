import sys
sys.stdin=open("input.txt","r")
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1 #word를 p라는 dictionary의 key 값으로
for i in range(n-1):
    word=input()
    p[word]=0 #쓰인 단어를 0으로 체크 
for key, val in p.items():
    if val==1:
        print(key)
        break
print(p)