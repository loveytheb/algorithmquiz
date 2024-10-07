import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(start):
    stack = [start]
    while stack:
        now_v = stack.pop()

        if visited[now_v] or now_v in is_bear:
            continue
        visited[now_v] = True

        # 더 이상 갈 수 없는 정점이면 yes를 출력
        if not graph[now_v]:
            print("yes")
            exit(0)

        for next_v in graph[now_v]:
            if not visited[next_v]:
                stack.append(next_v)

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S = int(input())
    is_bear = set(map(int, input().split()))

    dfs(1)
    print("Yes")