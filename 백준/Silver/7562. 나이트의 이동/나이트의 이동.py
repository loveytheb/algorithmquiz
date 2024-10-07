import sys
from collections import deque
input = sys.stdin.readline

# 나이트가 이동할 수 있는 8가지 방향을 정의
# (x축, y축) 기준으로 이동할 수 있는 상대적인 위치를 저장
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(l, start, end):
    # 체스판 크기가 l x l 이므로 l을 기준으로 visited 배열을 초기화
    # 각 위치를 방문했는지 여부를 기록하는 배열 (False로 초기화)
    visited = [[False] * l for _ in range(l)]
    
    # BFS에서 사용할 큐를 생성 (시작 위치와 거리 0을 함께 저장)
    queue = deque([start])
    
    # 시작 위치는 이미 방문한 상태이므로 방문 표시
    visited[start[0]][start[1]] = True
    
    while queue:
        # 큐에서 가장 앞에 있는 좌표와 이동 거리를 꺼냄
        x, y, dist = queue.popleft()
        
        # 현재 위치가 도착 지점과 같으면 이동 거리를 반환
        if (x, y) == end:
            return dist
        
        # 나이트가 이동할 수 있는 8가지 방향에 대해 탐색
        for i in range(8):
            # 새로운 좌표를 계산 (현재 좌표에 이동 방향을 더함)
            nx, ny = x + dx[i], y + dy[i]
            
            # 새 좌표가 체스판 범위 내에 있고, 아직 방문하지 않은 경우
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                # 방문한 것으로 표시
                visited[nx][ny] = True
                # 새 좌표와 이동 거리를 큐에 추가 (이전 거리 + 1)
                queue.append((nx, ny, dist + 1))

t = int(input())  # 테스트 케이스의 수를 입력받음

for _ in range(t):
    l = int(input())  # 체스판의 크기 (l x l)
    
    # 시작 위치 좌표 입력 (0 <= x, y < l)
    start = tuple(map(int, input().split()))  # 시작 좌표 (x, y)
    
    # 도착 위치 좌표 입력 (0 <= x, y < l)
    end = tuple(map(int, input().split()))  # 도착 좌표 (x, y)
    
    # 시작 위치와 도착 위치가 동일한 경우는 이동할 필요가 없으므로 0을 출력
    if start == end:
        print(0)
    else:
        # BFS 실행 후 결과 출력 (최소 이동 횟수)
        print(bfs(l, (start[0], start[1], 0), end))
