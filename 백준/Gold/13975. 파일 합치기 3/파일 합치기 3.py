import sys
import heapq

input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수

for _ in range(t):
    k = int(input()) # 파일의 개수
    file_sizes = list(map(int, input().split()))
    heapq.heapify(file_sizes) # 리스트를 최소 힙으로 변환
    total_cost = 0 # 총 비용
    
    while len(file_sizes) > 1: # 파일이 한 개만 남을 때까지 반복        
        # 크기가 가장 작은 두 파일 꺼내서 합침
        merge_cost = heapq.heappop(file_sizes) + heapq.heappop(file_sizes) 
        total_cost += merge_cost # 합친 비용 누적
        
        heapq.heappush(file_sizes, merge_cost) # 합쳐진 파일 힙에 다시 추가
    
    print(total_cost)