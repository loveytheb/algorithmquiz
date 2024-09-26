import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().strip().split() # 명령어를 입력받아 처리
    if command[0] == 'push':
        stack.append(int(command[1])) # 스택에 정수 X 추가
    elif command[0] == 'pop':
        if stack:
            print(stack.pop()) # 스택의 가장 위의 값 출력 후 제거
        else:
            print(-1) # 스택이 비어있다면 -1 출력
    elif command[0] == 'size':
        print(len(stack)) # 스택의 크기 출력
    elif command[0] == 'empty':
        print(1 if not stack else 0) # 스택이 비어있으면 1, 아니면 0 출력
    elif command[0] == 'top':
        if stack:
            print(stack[-1]) # 스택의 가장 위의 값 출력
        else:
            print(-1) # 스택이 비어있다면 -1 출력
