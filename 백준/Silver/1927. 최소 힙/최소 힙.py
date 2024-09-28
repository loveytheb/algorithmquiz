import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 명령 개수
min_heap = [] # 최소 힙 생성

for _ in range(N): # 명령의 개수만큼 반복
    x = int(input()) # 각 명령 입력 받음
    if x == 0: # 힙에서 값을 꺼내야 할 경우
        if min_heap: # 힙에 값이 있을 때
            print(heapq.heappop(min_heap)) #최소값 출력 후 삭제
        else: # 힙이 비어있는 경우
            print(0) # 0 출력
    else: # x가 0이 아닐 경우, 힙에 값 추가
        heapq.heappush(min_heap, x)

# 시간 복잡도 O(N log N)