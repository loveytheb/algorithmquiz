import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 목표지점에 도달한 경우
        if x == N - 1 and y == N - 1:
            print("HaruHaru")
            return 
        
        # (x, y)에서 점프할 수 있는 거리를 가져옴
        jump = board[x][y]
        
        # 오른쪽으로 이동 (x, y + jump)
        if y + jump < N and not visited[x][y + jump]:
            visited[x][y + jump] = True
            queue.append((x, y + jump))
        
        # 아래로 이동 (x + jump, y)
        if x + jump < N and not visited[x + jump][y]:
            visited[x + jump][y] = True
            queue.append((x + jump, y))
    
    # 큐를 모두 탐색한 뒤에도 목표지점에 도달하지 못했다면
    print("Hing")


bfs(0, 0)