n, m = list(map(int, input().split(' '))) # 떡의 갯수n와 요청한 떡의 길이m을 입력

array = list(map(int, input().split())) # 떡의 개별 높이 정보를 입력

start = 0 # 이진 탐색을 위한 시작점과
end = max(array) #끝점 설정 (가장 긴 떡의 길이)

result =0 #이진탐색 수행 (반복적)
while(start <= end):
    total = 0
    mid = (start+end) // 2 #현재 우리가 자르고자 하는 그 높이 자체
    for x in array: # x는 현재 떡의 길이
        if x > mid: #잘랐을 때 떡의 양 계산
            total += x-mid #잘린 부분의 떡을 토탈 변수에 담을 수 있도록 해서 전체 떡을 잘랐을 때 떡의 양 전부가 담길 수 있도록 함
    if total < m : #떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        end = mid -1 #높이 값이 줄어드는 방향으로 탐색 범위를 조정
    else:#떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 에 기록
        start = mid + 1 

print(result) #정답 출력        



