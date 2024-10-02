import sys

input = sys.stdin.readline # 입력을 빠르게 받기 위한 설정
T = int(input()) # 테스트 케이스 수 입력

for _ in range(T): # 각 테스트 케이스 처리
    A, B = map(int, input().split()) # 두 정수 A와 B 입력
    
    while True: # 무한 루프
        if A > B: # A가 B보다 클 경우
            A //= 2 # A를 반으로
        elif A < B: # A가 B보다 작을 경우
            B //= 2 # B를 반으로
        else: # A와 B가 같을 경우
            print(A * 10) # 결과 출력
            break