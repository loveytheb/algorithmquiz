from collections import deque
import sys

# 상, 하, 좌, 우 네 방향 이동을 위한 좌표 설정
dx = [-1, 1, 0, 0]  # x좌표 이동 방향 (위, 아래)
dy = [0, 0, -1, 1]  # y좌표 이동 방향 (왼쪽, 오른쪽)

def bfs(x, y):
    sheep, wolf = 0, 0  # 로컬 변수로 양과 늑대 수 초기화
    queue = deque()  # BFS에 사용할 큐 선언
    queue.append((x, y))  # 시작 위치를 큐에 추가
    visited[x][y] = True  # 시작 위치를 방문한 것으로 표시
    
    # 현재 시작 위치에서 양과 늑대 세기
    if field[x][y] == 'k':  # 시작 위치가 양일 경우
        sheep += 1  # 양 개수 증가
    elif field[x][y] == 'v':  # 시작 위치가 늑대일 경우
        wolf += 1  # 늑대 개수 증가
    
    # BFS로 탐색 시작
    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # 큐에서 가장 앞에 있는 좌표를 꺼내서 현재 위치로 설정
        
        # 4방향 탐색
        for i in range(4):  # 상, 하, 좌, 우 방향을 차례로 확인
            nx, ny = x + dx[i], y + dy[i]  # 다음 탐색할 좌표 설정
            # 유효한 좌표인지 확인 (맵을 벗어나지 않고, 방문하지 않았으며, 울타리가 아닌 경우)
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] != '#':
                visited[nx][ny] = True  # 새로운 좌표를 방문한 것으로 표시
                queue.append((nx, ny))  # 해당 좌표를 큐에 추가하여 다음 탐색 대상으로 설정
                
                # 양과 늑대 세기
                if field[nx][ny] == 'k':  # 해당 좌표가 양일 경우
                    sheep += 1  # 양 개수 증가
                elif field[nx][ny] == 'v':  # 해당 좌표가 늑대일 경우
                    wolf += 1  # 늑대 개수 증가

    # 한 구역 탐색이 끝난 후 양과 늑대 비교
    if wolf >= sheep:  # 늑대가 더 많거나 같으면
        sheep = 0  # 양은 모두 잡아먹힘
    else:  # 양이 더 많으면
        wolf = 0  # 늑대는 전부 쫓겨남

    return sheep, wolf  # 해당 구역에서 남은 양과 늑대 수 반환


input = sys.stdin.readline                    
R, C = map(int, input().split())  # 행(R), 열(C) 크기 입력 받기
field = [list(input().strip()) for _ in range(R)]  # 필드를 R x C 크기의 2차원 리스트로 입력받기
visited = [[False] * C for _ in range(R)]  # 방문 여부를 기록하는 R x C 크기의 2차원 리스트 초기화

total_sheep, total_wolf = 0, 0  # 최종적으로 살아남은 양과 늑대의 수를 저장할 변수 초기화

# 모든 좌표에서 BFS 수행
for i in range(R):  # 맵의 모든 행을 순회
    for j in range(C):  # 맵의 모든 열을 순회
        # 해당 좌표가 아직 방문하지 않았고 울타리가 아닌 경우에만 BFS 수행
        if not visited[i][j] and field[i][j] in ('k', 'v'):  # 양이나 늑대가 있는 곳만 탐색
            sheep, wolf = bfs(i, j)  # 해당 좌표에서 BFS 시작
            
            # 영역 탐색이 끝난 후, 남은 양과 늑대 수를 최종 결과에 반영
            total_sheep += sheep
            total_wolf += wolf

print(total_sheep, total_wolf)  # 최종적으로 살아남은 양과 늑대의 수 출력