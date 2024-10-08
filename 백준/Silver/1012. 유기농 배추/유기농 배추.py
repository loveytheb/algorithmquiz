import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우 이동을 위한 좌표 변화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 배추밭 범위 내에 있고, 배추가 있으며, 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    # 가로 길이 M, 세로 길이 N, 배추 위치의 개수 K
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)] # 배추밭 초기화
    visited = [[False] * M for _ in range(N)] # 방문 여부 체크
    
    for _ in range(K): # 배추가 심어진 위치 입력
        y, x = map(int, input().split())
        field[x][y] = 1 # 배추 위치 표시
    
    count = 0 # 배추 군락의 개수
    
    # 모든 배추밭 탐색
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]: # 배추가 있고 방문하지 않았을 때
                bfs(i, j) # 새로운 군락 탐색
                count += 1 # 군락 개수 증가
    
    print(count)