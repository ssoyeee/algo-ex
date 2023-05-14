# 6의 약수는 1,2,3,6 총 네개
# n의 약수들 중 k번째로 작은 수 출력: 
# 6 3 이면 6의 약수들 중 3번째로 작은 수 
# k번째 약수가 존재하지 않으면 -1 출력


import sys
# txt file 읽기
sys.stdin = open("input.txt","rt")

# 두 수 받아오기
n, k = map(int, input().split())
# 갯수세기
cnt = 0

# 약수 찾기
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k: #k번째 약수를 발견하면 출력
        print(i) 
        break
else: 
    print(-1)

