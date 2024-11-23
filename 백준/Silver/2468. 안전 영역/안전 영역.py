import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, height, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and field[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    

max_height = max(map(max, field))
max_safe_areas = 0 # 최대 높이 안전 영역

for height in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0 # 현재 높이 안전 영역
    
    for i in range(N):
        for j in range(N):
            # 방문하지 않았고, 물에 잠기지 않은 경우 탐색
            if not visited[i][j] and field[i][j] > height:
                bfs(i, j, height, visited)
                safe_areas += 1
                
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)