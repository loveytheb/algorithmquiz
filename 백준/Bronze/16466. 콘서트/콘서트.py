import sys
input = sys.stdin.readline

N = int(input()) # 1차에서 이미 팔린 티켓 수
sold_tickets = list(map(int, input().split())) # 판매된 티켓 번호 list에 입력

sold_tickets.sort() # 판매된 티켓 번호 정렬

# 1부터 시작해서 판매되지 않은 가장 작은 티켓 번호 찾기
ticket_num = 1 # 티켓 번호 1부터 시작

for ticket in sold_tickets:
    # 현재 티켓 번호가 판매된 티켓 번호와 같은 경우
    if ticket == ticket_num:
        ticket_num += 1 # 다음 번호로 이동
        
print(ticket_num)