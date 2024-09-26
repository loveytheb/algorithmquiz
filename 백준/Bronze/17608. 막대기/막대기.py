import sys
input = sys.stdin.readline

N = int(input())
stack = []

# 막대기의 높이 입력 받은 순서대로 stack에 저장
for _ in range(N):
    stack.append(int(input()))

count = 0
max_height = 0

for height in reversed(stack):
    if height > max_height:
        count += 1
        max_height = height

print(count)