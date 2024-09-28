import sys
import heapq
input = sys.stdin.readline

# 선물의 가치를 저장할 최대 힙
gifts = []
output = []

n = int(input())  # 아이들과 거점지를 방문한 횟수

for _ in range(n):
    data = list(map(int, input().split()))
    a = data[0]  # 선물의 개수
    
    if a == 0:
        # 아이들을 만난 경우
        if gifts:
            # 가장 큰 선물 가치 출력
            output.append(-heapq.heappop(gifts))  # 최대 힙이므로 음수로 저장
        else:
            output.append(-1)  # 선물이 없는 경우
    else:
        # 선물의 가치를 충전하는 경우
        for value in data[1:a + 1]:
            heapq.heappush(gifts, -value)  # 최대 힙을 위해 음수로 저장

# 결과 출력
print('\n'.join(map(str, output)))
