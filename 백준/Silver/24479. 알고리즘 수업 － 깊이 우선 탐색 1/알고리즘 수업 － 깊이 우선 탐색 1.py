import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

def dfs(graph, v, visited, count):
    visited[v] = count # 방문 순서 저장
    for u in sorted(graph[v]): # 정점 v에 연결된 모든 정점 u
        if visited[u] == 0: # 아직 방문하지 않았다면
            count = dfs(graph, u, visited, count + 1) # 다음 정점 방문
    return count

n, m, r = map(int, input().split()) # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 각 정점의 방문 여부

# 간선 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 시작
dfs(graph, r, visited, 1)

# 방문 순서 출력
for i in range(1, n + 1):
    print(visited[i])