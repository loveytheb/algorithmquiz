from collections import deque
import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(5)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향
unique_numbers = set()  # 중복 숫자를 제거하기 위한 집합

def bfs():
    # BFS 큐 초기화
    queue = deque()
    
    # 초기 위치에서 시작 (모든 칸에서 시작)
    for i in range(5):
        for j in range(5):
            # (x, y, path) 형태로 큐에 추가
            queue.append((i, j, str(board[i][j])))

    while queue:
        x, y, path = queue.popleft()  # 큐에서 현재 위치와 숫자 경로를 꺼냄
        
        # 이동 횟수가 5번일 경우, 6자리 숫자를 완성
        if len(path) == 6:
            unique_numbers.add(path)  # 만들어진 숫자를 집합에 추가
            continue
        
        # 상하좌우로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 다음 이동 좌표 계산
            if 0 <= nx < 5 and 0 <= ny < 5:  # 숫자판 경계를 벗어나지 않는지 확인
                queue.append((nx, ny, path + str(board[nx][ny])))  # 다음 위치로 이동하며 숫자 추가

# BFS 실행
bfs()

print(len(unique_numbers))
