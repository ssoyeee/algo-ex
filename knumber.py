# N개의 숫자로 이루어진 숫자열이 주어지면, 
# 해당 숫자열중에서 s번째~0번째까지의 수를 오름차순 정렬 후
# k번째로 나타나는 숫자 출력

from posixpath import split
import sys
sys.stdin=open("input.txt","rt")

T=int(input())
for t in range(T):
    n, s, e, k = map(int, input().split()) #s와 e는 번째임
    a = list(map(int, input().split())) # 각 케이스의 자료 가져오기
    #list는 첫 자료가 0번에 들어가 있음 두번째 자료는 1번일 것
    # ex------>print(a[1:5]) #1번 index부터 4번 index까지 출력
    a = a[s-1:e]
    a.sort() #오름차순
    print("#%d %d" %(t+1, a[k-1])) #케이스번호:t, k는 k번째 나타나는 수 의미
