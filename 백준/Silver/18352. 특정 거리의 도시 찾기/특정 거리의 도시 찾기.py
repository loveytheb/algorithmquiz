import sys
from collections import deque
input = sys.stdin.readline

# BFS 탐색을 통해 시작 도시로부터 각 도시에 대한 최단 거리를 계산하는 함수
def bfs(start, graph, distance, k):
    # 시작 도시는 거리가 0이므로 초기화
    queue = deque([start])
    distance[start] = 0  # 시작 도시의 거리는 0으로 설정

    while queue:
        # 큐에서 가장 앞에 있는 도시를 꺼냄
        current = queue.popleft()

        # 현재 도시에서 연결된 모든 도시 탐색
        for next_city in graph[current]:
            # 아직 방문하지 않은 도시인 경우에만 처리
            if distance[next_city] == -1:
                # 현재 도시까지의 거리 + 1로 갱신
                distance[next_city] = distance[current] + 1
                queue.append(next_city)

# 거리 K인 도시들을 찾고 출력하는 함수
def find_cities_with_distance_k(n, m, k, x, roads):
    # 도시들의 연결 정보를 저장할 그래프 초기화 (1번 도시부터 시작, 0번 도시는 사용하지 않음)
    graph = [[] for _ in range(n + 1)]

    # 도로 정보 입력 (단방향 그래프)
    for a, b in roads:
        graph[a].append(b)  # a에서 b로 가는 단방향 도로

    # 모든 도시의 거리를 -1로 초기화 (-1은 아직 방문하지 않은 도시를 의미)
    distance = [-1] * (n + 1)

    # BFS 실행하여 시작 도시로부터 각 도시까지의 최단 거리를 계산
    bfs(x, graph, distance, k)

    # 거리 K인 도시들을 찾아서 결과 리스트에 저장
    result = []
    for i in range(1, n + 1):  # 도시 번호는 1부터 시작
        if distance[i] == k:  # 거리가 k인 도시를 찾음
            result.append(i)

    # 결과 출력
    if result:
        # 거리 K인 도시가 존재하는 경우, 도시 번호를 오름차순으로 정렬 후 출력
        result.sort()
        for city in result:
            print(city)
    else:
        # 거리 K인 도시가 없는 경우 -1 출력
        print(-1)

n, m, k, x = map(int, input().split())  
# n: 도시 수, m: 도로 수, k: 찾고자 하는 거리, x: 시작 도시 번호

# 도로 정보 입력
# 예: roads는 (a, b) 형태의 튜플로 a 도시에서 b 도시로 가는 단방향 도로
roads = [tuple(map(int, input().split())) for _ in range(m)]

# 거리 K인 도시들을 찾아서 출력하는 함수 호출
find_cities_with_distance_k(n, m, k, x, roads)