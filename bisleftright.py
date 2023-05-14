# count_by_range라이브러리는 bisect_left와 bisect_right을 이용해서 값이 left value 이상, right value 이하인 값을 모두 찾을 수 있다
# bisect

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value): #값이 [left_value, right_value]인 데이터 갯수를 반환하는 함수
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index

n,x = map(int, input().split()) # 데이터의 갯수 n, 찾고자하는 값 x입력받기
array = list(map(int, input().split())) #전체 데이터 입력받기

count = count_by_range(array, x, x) #값이 [x, x] 범위에 있는 데이터 수 계산

if count == 0 : #값이 x인 원소가 존재하지 않는다면
    print(-1)
else: #값이 x인 원소가 존재한다면
    print(count)

