import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 나무 수, M: 필요한 나무 길이
tree_heights = list(map(int, input().split())) # 나무들의 높이 리스트

# 이분 탐색을 위한 변수 설정
start, end = 0, max(tree_heights) # 절단기 높이의 범위

# 이분 탐색 수행
def get_wood_amount(cut_height):
    # 절단기 높이 cut_height로 나무를 잘랐을 때 얻을 수 있는 나무의 총합 계산
    total = 0
    for tree in tree_heights:
        if tree > cut_height:
            total += tree - cut_height # 잘린 나무 길이를 더함
    return total

result = 0 # 최대 절단기 높이 저장 변수

while start <= end:
    mid = (start + end) // 2 # 중간값을 절단기 높이로 설정
    wood = get_wood_amount(mid) # 현재 절단기 높이에서 가져올 수 있는 나무 길이 계산

    if wood >= M: # 나무가 충분히 잘렸다면
        result = mid # 절단기 높이 저장
        start = mid + 1 # 더 높은 절단기 높이를 탐색
    else:
        end = mid - 1 # 나무가 부족하다면 더 낮은 절단기 높이를 탐색

# 결과 출력
print(result)