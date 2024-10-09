import heapq

def solution(scoville, K):
    # 리스트 최소 힙으로 변환
    heapq.heapify(scoville)
    count = 0
    # 스코빌 지수가 남아있고, 가장 작은 스코빌 지수가 k보다 작을 때까지만 반복
    while len(scoville) > 1 and scoville[0] < K:
        # 스코빌 지수 가장 낮은 두 개의 음식을 섞는 방법
        new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_scoville) # 새로운 스코빌 지수 다시 힙에 추가
        count += 1
    
    if scoville[0] >= K:
        return count
    else:
        return -1