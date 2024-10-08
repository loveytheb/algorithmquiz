import sys
from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    # 최대 이동 범위: N과 K의 최댓값
    max = 100000
    # 각 위치 별로 몇 초 만에 도착했는지 기록
    visited = [0] * (max + 1)
    
    queue = deque([N])
    
    while queue:
        current = queue.popleft()
        
        if current == K: # 동생 위치에 도달하면 그때까지의 시간 반환
            return visited[current]
        
        # 세 가지 이동 경우에 대해 탐색
        for next_position in (current - 1, current + 1, current * 2):
            # 이동할 위치가 범위 내에 있고, 방문한 적 없는 경우
            if 0 <= next_position <= max and not visited[next_position]:
                visited[next_position] = visited[current] + 1
                queue.append(next_position)

print(bfs(N, K))                