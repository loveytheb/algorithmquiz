import sys
from collections import Counter
input = sys.stdin.readline

N = int(input()) # 수의 개수
nums = [int(input()) for _ in range(N)] # N개의 정수

# 1. 산술 평균
mean = round(sum(nums) / N)
print(mean)

# 2. 중앙값
nums.sort()
median = nums[N // 2]
print(median)

# 3. 최빈값
cnt = Counter(nums) # 빈도 계산
mode = cnt.most_common() # 빈도수가 높은 순으로 정렬

if len(mode) > 1:
    if mode[0][1] == mode[1][1]: # 빈도수가 같으면 두 번째로 작은 값
        mode_value = sorted([mode[0][0], mode[1][0]])[1]
    else:
        mode_value = mode[0][0] # 최빈값 하나면 첫 번째 값 선택
else:
    mode_value = mode[0][0] # N이 1일 때는 첫 번째 값
print(mode_value)

# 4. 범위
range_value = max(nums) - min(nums)
print(range_value)