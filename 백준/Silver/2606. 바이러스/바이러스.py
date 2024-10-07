import sys
input = sys.stdin.readline

def dfs(graph, visited, start):
    # 현재 컴퓨터(노드)를 방문 처리
    visited[start] = True

    # 현재 컴퓨터와 연결된 다른 컴퓨터들을 탐색
    for next_computer in graph[start]:
        # 만약 연결된 컴퓨터를 아직 방문하지 않았다면, 재귀적으로 DFS 수행
        if not visited[next_computer]:
            dfs(graph, visited, next_computer)

n = int(input())  # 컴퓨터의 수 (노드 수)
m = int(input())  # 연결된 컴퓨터 쌍의 수 (간선 수)

# 그래프 초기화 (1번 컴퓨터부터 n번 컴퓨터까지를 나타냄, 0번 인덱스는 사용하지 않음)
graph = [[] for _ in range(n + 1)]

# 입력받은 연결 정보를 바탕으로 그래프 생성
for _ in range(m):
    a, b = map(int, input().split())  # a와 b는 서로 연결된 컴퓨터
    graph[a].append(b)  # a에서 b로 가는 간선을 추가
    graph[b].append(a)  # b에서 a로 가는 간선도 추가 (양방향 그래프)

# 각 컴퓨터의 방문 여부를 저장하는 리스트
# 초기에는 모든 컴퓨터가 방문되지 않았으므로 False로 초기화
visited = [False] * (n + 1)

# 1번 컴퓨터에서 바이러스가 시작되므로, DFS를 통해 연결된 모든 컴퓨터를 감염시킴
dfs(graph, visited, 1)

# 1번 컴퓨터를 제외한 감염된 컴퓨터의 수를 출력
# visited 리스트에서 True의 개수를 세고, 1번 컴퓨터는 제외해야 하므로 -1
print(visited.count(True) - 1)