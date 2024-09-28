import sys
import heapq

input = sys.stdin.readline

# N: 센티 제외 거인나라 인구 수, Hcenti: 센티의 키, T: 마법 뿅망치의 횟수 제한
N, Hcenti, T = map(int, input().split())
Hgiants = [-int(input()) for _ in range(N)]  # 거인들의 키 음수로 변환한 목록
count = 0  # 마법의 뿅망치 사용 횟수

heapq.heapify(Hgiants)  # 최대 힙으로 변환

for _ in range(T):  # T번 동안 마법의 뿅망치 사용
    if -Hgiants[0] == 1 or -Hgiants[0] < Hcenti:
        break
    else:
        heapq.heapreplace(Hgiants, -(-Hgiants[0] // 2))
        count += 1
        
if -Hgiants[0] >= Hcenti:
    print('NO')
    print(-Hgiants[0])
else:
    print('YES')
    print(count)