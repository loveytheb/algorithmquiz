import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start]) # 시작 정점을 큐에 넣음
    visited[start] = 1 # 첫번째 정점 방문 순서 저장
    count = 2 # 다음 정점을 방문할 때 사용할 카운트(1은 시작 정점에 사용됨)
    
    while queue:
        v = queue.popleft() # 큐에서 정점을 하나 뽑아냄
        for u in sorted(graph[v]): # 정점 v에 연결된 정점 u를 오름차순으로 방문
            if visited[u] == 0: # 아직 방문하지 않았아면
                visited[u] = count # 방문 순서 저장
                count += 1 # 카운트 증가시켜 다음 정점에 부여
                queue.append(u) # 다음 탐색을 위해 큐에 추가
                
n, m, r = map(int, input().split()) # 정점 수, 간선 수, 시작 정점 입력 받기
graph = [[] for _ in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 각 정점의 방문 여부와 방문 순서 저장

# 간선 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS 시작
bfs(graph, r, visited)

# 방문 순서 출력
for i in range(1, n + 1):
    print(visited[i])