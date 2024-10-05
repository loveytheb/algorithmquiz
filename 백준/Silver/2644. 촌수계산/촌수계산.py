from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 사람의 수
a, b = map(int, input().split()) # 촌수를 계산할 두 사람
m = int(input()) # 부모-자식 관계의 수

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 부모-자식 관계 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    # 양방향 그래프
    graph[x].append(y)
    graph[y].append(x)

# BFS 함수 정의
def bfs(start, target):
    queue = deque([(start, 0)]) # (현재 사람, 촌수)로 저장
    visited = [False] * (n + 1) # 방문 여부 체크
    visited[start] = True

    while queue:
        person, count = queue.popleft()

        if person == target: # 목표 사람에 도달하면 촌수 반환
            return count

        for relative in graph[person]: # 현재 사람과 연결된 모든 사람 탐색
            if not visited[relative]:
                visited[relative] = True
                queue.append((relative, count + 1)) # 촌수를 증가시켜 큐에 추가

    return -1 # 목표 사람에 도달할 수 없으면 -1 반환

print(bfs(a, b))