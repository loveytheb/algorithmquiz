import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_y, start_x):
    # BFS 탐색을 위한 큐 초기화
    queue = deque()
    # 시작 좌표 (헛간(B))를 큐에 추가
    queue.append((start_y, start_x))
    # 헛간(B) 위치의 거리를 0으로 설정 (시작점)
    graph[start_y][start_x] = 0  
    
    while queue:
        # 큐에서 현재 위치를 꺼냄
        current_y, current_x = queue.popleft()  
        
        # 상, 하, 좌, 우 방향으로 탐색
        for direction_y, direction_x in directions:  
            # 새로운 좌표 계산
            next_y, next_x = current_y + direction_y, current_x + direction_x
            
            # 새로운 좌표가 격자 내에 있는지 확인
            if (0 <= next_y < 10) and (0 <= next_x < 10):
                # 새로운 좌표가 호수(L)인 경우
                if graph[next_y][next_x] == 'L':  
                    # 현재 좌표까지의 거리를 반환 (호수에 도달)
                    return graph[current_y][current_x]  
                
                # 새로운 좌표가 이동 가능한 칸인 경우 ('.'인 경우)
                if graph[next_y][next_x] == '.':  
                    # 새로운 좌표를 큐에 추가하여 다음 탐색을 위해 준비
                    queue.append((next_y, next_x))  
                    # 현재 좌표까지의 거리 + 1로 새로운 좌표의 거리를 설정
                    graph[next_y][next_x] = graph[current_y][current_x] + 1  

# 10x10 격자 입력 받기
graph = [list(input().strip()) for _ in range(10)]  
# 상, 하, 좌, 우 방향을 나타내는 방향 벡터
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

# 격자를 순회하여 헛간(B)의 위치 찾기
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':  # 헛간(B) 위치 발견
            # BFS를 통해 호수(L)까지의 최소 거리 찾기
            min_cows_needed = bfs(i, j)  

# 최소 소의 수를 출력
print(min_cows_needed)  