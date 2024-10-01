import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # n개의 정보
queue = deque() # 대기 줄 관리하는 큐 (큐는 FIFO 방식이기 때문에 먼저 도착한 학생이 먼저 식사를 한다는 조건과 일치함)
max_cnt = 0 # 대기하는 최대 학생 수
last_num = 0 # 맨 뒤에 대기 중인 학생 번호

for _ in range(n):
    info = input().split()
    
    if info[0] == '1': # 유형 1 : a인 학생 1명이 학교 식당에 도착하여 식당 입구의 맨 뒤에 줄을 선다.
        student_num = int(info[1])
        queue.append(student_num)
        
        current_cnt = len(queue) # 현재 대기 학생 수
    
        if current_cnt > max_cnt: # 대기 인원이 최대일 경우
            max_cnt = current_cnt
            last_num = student_num
        elif current_cnt == max_cnt: # 대기 인원이 최대 학생 수와 같다면 학생의 번호가 가장 작은 경우 선택
            last_num = min(last_num, student_num)
    elif info[0] == '2': # 유형 2 : 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사 시작
        queue.popleft() #큐에서 맨 앞 학생 제거

print(max_cnt, last_num)