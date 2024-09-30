import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 게임판 크기
graph = [list(map(int, input().split())) for _ in range(n)] # N x N 크기의 게임판
visited = [[0] * n for _ in range(n)] # 방문 기록 배열 초기화
dx = [0, 1] # 오른쪽으로 이동
dy = [1, 0] # 아래쪽으로 이동

def bfs(x, y):
    queue = deque([(x, y)]) # 시작점 (x, y)을 큐에 넣음
    while queue:
        x, y = queue.popleft() # 큐의 맨 앞에 있는 좌표를 꺼냄
        if (x, y) == (n - 1, n - 1): # 목표 지점에 도착했는지 확인
            return 1 # 도착했다면 1을 반환
        
        for i in range(2): # 오른쪽과 아래쪽 두 방향에 대해 탐색
            nx = x + dx[i] * graph[x][y] # x축 이동
            ny = y + dy[i] * graph[x][y] # y축 이동
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]: # 범위 내에 있고 방문하지 않았다면
                queue.append((nx, ny)) # 큐에 새 좌표 추가
                visited[nx][ny] = 1 # 해당 좌표를 방문했음을 기록
    return 0 # 큐가 비었을 때까지 목표 지점에 도착하지 못했다면 0을 반환


print("HaruHaru" if bfs(0, 0) else "Hing")