from collections import deque

def count_grass():
    R, C = map(int, input().split())
    field = [list(input().strip()) for _ in range(R)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동 정의
    visited = [[False] * C for _ in range(R)] # 방문 여부를 저장 배열

    def bfs(x, y):
        queue = deque([(x, y)]) # 시작점 추가
        visited[x][y] = True  # 현재 위치 방문 처리

        while queue:
            cx, cy = queue.popleft() # 현재 위치 꺼냄

            for dx, dy in directions: # 상하좌우 탐색
                nx, ny = cx + dx, cy + dy # 이동할 좌표 계산

                # 범위 내에 있고, 아직 방문하지 않았으며, 풀일 경우
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] == '#':
                    visited[nx][ny] = True # 방문 처리
                    queue.append((nx, ny)) # 큐에 추가

    count = 0 # 덩어리 개수

    for i in range(R):
        for j in range(C):
            if field[i][j] == '#' and not visited[i][j]: # 방문하지 않은 덩어리를 발견하면
                bfs(i, j) # BFS로 연결된 덩어리 탐색
                count += 1 # 덩어리 개수 증가

    print(count)

count_grass()
