import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 게임판 크기 입력
graph = [list(map(int, input().split())) for _ in range(n)]  # 게임판 입력
visited = [[0] * n for _ in range(n)]  # 방문 기록 배열 초기화
dx = [0, 1]  # 오른쪽으로 이동
dy = [1, 0]  # 아래쪽으로 이동

def bfs(x, y):
    queue = deque([(x, y)]) # 시작점 (x, y)을 큐에 넣기
    while queue:
        x, y = queue.popleft() # 큐의 맨 앞에 있는 좌표를 꺼내고
        if (x, y) == (n - 1, n - 1): # 목표 지점에 도착했다면
            return 1  # 1을 반환해 성공을 알립니다.
        
        # 오른쪽, 아래쪽 두 방향에 대해 탐색합니다.
        for i in range(2):
            nx = x + dx[i] * graph[x][y]  # x좌표에서 이동
            ny = y + dy[i] * graph[x][y]  # y좌표에서 이동
            
            # 범위 내에 있고 방문하지 않았다면 이동
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny))  # 새로 이동한 좌표를 큐에 넣기
                visited[nx][ny] = 1  # 방문 기록을 남기기
    return 0 # 끝까지 탐색했으나 도착하지 못한 경우 0 반환

print("HaruHaru" if bfs(0, 0) else "Hing")