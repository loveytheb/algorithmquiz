import sys
input = sys.stdin.readline

N = int(input()) # N개의 좌표
X = list(map(int, input().split())) # 좌표 입력 받기
arr = sorted(set(X)) # 중복 제거 후 정렬된 좌표 리스트

dic = {} # 좌표 압축 결과를 저장할 딕셔너리

# 정렬된 좌표 리스트를 순회하며 인덱스를 딕셔너리에 저장
for index, value in enumerate(arr):
    dic[value] = index # 각 좌표에 대해 압축된 값을 인덱스로 저장

result = [dic[X] for X in X] # 원래 좌표를 압축된 값으로 표현

print(' '.join(map(str, result)))