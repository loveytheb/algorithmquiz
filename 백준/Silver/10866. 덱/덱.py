from collections import deque  # 덱 사용을 위해 deque 불러오기
import sys                     # 입력을 빠르게 처리하기 위해 sys 사용

input = sys.stdin.readline     # 입력을 빠르게 받기 위한 설정

# 덱 선언
dq = deque()

# 명령어 수 입력
N = int(input())

# 명령어 처리
for _ in range(N):
    command = input().split()  # 명령어를 입력받고 공백 기준으로 나눔
    
    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))  # 덱 앞에 숫자 추가
    
    elif command[0] == 'push_back':
        dq.append(int(command[1]))  # 덱 뒤에 숫자 추가
    
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())  # 덱 앞에서 숫자 빼기
        else:
            print(-1)  # 덱이 비어있으면 -1 출력
    
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())  # 덱 뒤에서 숫자 빼기
        else:
            print(-1)  # 덱이 비어있으면 -1 출력
    
    elif command[0] == 'size':
        print(len(dq))  # 덱에 있는 원소 개수 출력
    
    elif command[0] == 'empty':
        print(1 if not dq else 0)  # 덱이 비어있으면 1, 아니면 0 출력
    
    elif command[0] == 'front':
        if dq:
            print(dq[0])  # 덱 앞쪽에 있는 숫자 출력
        else:
            print(-1)  # 덱이 비어있으면 -1 출력
    
    elif command[0] == 'back':
        if dq:
            print(dq[-1])  # 덱 뒤쪽에 있는 숫자 출력
        else:
            print(-1)  # 덱이 비어있으면 -1 출력
