import sys
input = sys.stdin.readline

N = int(input())  # 후보 수
dasom = int(input())  # 다솜이의 현재 득표 수
votes = [int(input()) for _ in range(N - 1)]  # 각 후보의 투표 수 저장
count = 0  # 매수해야 할 표 수

# 후보가 다솜 1명일 경우
if N == 1:
    print(0)
else:
    # 다솜이보다 높은 표 수가 있는 후보들의 득표 수 내림차순으로 정렬
    votes.sort(reverse=True)
    
    while votes[0] >= dasom: # 가장 높은 득표 수와 다솜의 현재 득표수 비교
        dasom += 1 # 다솜의 득표수 1 증가
        count += 1 # 매수 수 1 증가
        votes[0] -= 1 # 가장 높은 득표 수 1 감소
        votes.sort(reverse=True)
    
    print(count)