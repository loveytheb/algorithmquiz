from collections import deque
import sys

input = sys.stdin.readline

def count_floor_decoration():
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    floor = [list(input().strip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    def bfs(x, y, direction):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            cx, cy = queue.popleft()
            
            # 현재 방향에 따라 이동 가능한 곳 확인
            for dx, dy in direction:
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < N and 0 <= ny < M: # 범위 내에 있고
                    if not visited[nx][ny] and floor[nx][ny] == floor[cx][cy]: # 같은 종류의 판자이며, 아직 방문하지 않은 경우
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    count = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j]: # 방문하지 않은 칸 발견
                if floor[i][j] == '-': # 가로 판자
                    bfs(i, j, [(0, 1)]) # 오른쪽만 탐색
                elif floor[i][j] == '|': # 세로 판자
                    bfs(i, j, [(1, 0)]) # 아래쪽만 탐색

                count += 1 # 새로운 덩어리 발견
    
    print(count)

count_floor_decoration()