import sys
input = sys.stdin.readline

n = int(input())  # 배열의 크기
arr = list(map(int, input().split()))  # 배열
S = int(input())  # 교환 가능 횟수

for i in range(n):
    # 남은 횟수 내에서 최대값을 찾아서 앞으로 이동시킴
    max_idx = i
    for j in range(i + 1, min(n, i + S + 1)):
        if arr[j] > arr[max_idx]:
            max_idx = j

    # 최대값을 현재 위치로 옮기기 위해 교환
    for j in range(max_idx, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        S -= 1  # 교환 횟수 감소
        if S == 0:
            break  # 더 이상 교환할 수 없으면 중단

    if S == 0:
        break  # 교환 횟수가 다 소진되면 종료

print(' '.join(map(str, arr)))  # 정렬된 배열 출력