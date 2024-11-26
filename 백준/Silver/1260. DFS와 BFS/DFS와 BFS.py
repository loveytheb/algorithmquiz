from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 각 노드의 연결된 노드 오름차순 정렬 (작은 노드부터 방문하기 위해)
for i in range(1, N + 1):
    graph[i].sort()

# DFS
def dfs(V, visited, path):
    visited[V] = True
    path.append(V)
    
    for neighbor in graph[V]:
        if not visited[neighbor]:
            dfs(neighbor, visited, path)

# BFS
def bfs(V):
    queue = deque([V])
    visited = [False] * (N + 1)
    visited[V] = True
    path = []
    
    while queue:
        node = queue.popleft()
        path.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return path

# DFS 실행
dfs_path = []
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs, dfs_path)

# BFS 실행
bfs_path = bfs(V)

print(' '.join(map(str, dfs_path)))
print(' '.join(map(str, bfs_path)))