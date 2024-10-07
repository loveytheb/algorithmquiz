import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# DFS를 통해 두 노드 사이의 거리를 구하는 함수
def dfs(node, target, dist):
    if node == target:  # 목표 노드에 도착하면 현재까지 누적된 거리 반환
        return dist
    visited[node] = True  # 현재 노드 방문 처리

    for next_node, weight in graph[node]:
        if not visited[next_node]:  # 방문하지 않은 노드에 대해 DFS 진행
            result = dfs(next_node, target, dist + weight)
            if result != -1:  # 경로가 존재하면 바로 반환
                return result
    return -1  # 경로가 없으면 -1 반환

# 입력 처리
n, m = map(int, input().split())  # n은 노드의 수, m은 쿼리의 수
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 쿼리 처리
for _ in range(m):
    visited = [False] * (n + 1)
    u, v = map(int, input().split())
    print(dfs(u, v, 0))