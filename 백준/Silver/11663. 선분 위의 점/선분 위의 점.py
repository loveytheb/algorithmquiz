import sys
import bisect

# 입력 받기
input = sys.stdin.readline

# 점의 개수 N과 선분의 개수 M 입력 받기
N, M = map(int, input().split())

# 점들의 좌표 입력 받기
points = list(map(int, input().split()))

# 선분 정보 입력 받기
segments = [tuple(map(int, input().split())) for _ in range(M)]

# 점들을 오름차순으로 정렬
points.sort()

# 각 선분에 대해 점의 개수 계산
for left, right in segments:
    # right보다 작거나 같은 마지막 점의 인덱스를 찾음 (upper bound)
    right_index = bisect.bisect_right(points, right)
    # left보다 크거나 같은 첫 번째 점의 인덱스를 찾음 (lower bound)
    left_index = bisect.bisect_left(points, left)
    
    # 선분 [left, right]에 포함된 점의 개수 계산
    print(right_index - left_index)