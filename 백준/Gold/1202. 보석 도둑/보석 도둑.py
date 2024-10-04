import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 보석 총 개수, K: 가방 개수

jewels = [] # 보석 정보 리스트
for _ in range(N):
    M, V = map(int, input().split()) # M: 보석 무게, V: 보석 가격
    jewels.append((M, V))
    
bags = [] # 가방 최대 무게 리스트
for _ in range(K):
    C = int(input()) # 가방에 담을 수 있는 최대 무게
    bags.append(C)
    
# 보석과 가방을 무게 기준으로 오름차순 정렬
jewels.sort()
bags.sort()

max_heap = [] # 최대 힙 사용할 리스트
result = 0
jewel_index = 0

for bag in bags:
    # 현재 가방의 무게보다 작거나 같은 보석들을 최대 힙에 추가
    while jewel_index < N and jewels[jewel_index][0] <= bag:
        heapq.heappush(max_heap, -jewels[jewel_index][1]) # 최대 힙을 위해 가격에 - 부호를 붙임
        jewel_index += 1
    
    # 힙에서 가장 큰 값(즉, 가장 비싼 가격)을 꺼내서 결과에 더함    
    if max_heap:
        result += -heapq.heappop(max_heap)

print(result)