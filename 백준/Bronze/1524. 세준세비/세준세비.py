import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

for _ in range(T):
    input() # 각 테스트 케이스 줄 바꿈으로 구분
    N, M = map(int, input().split()) # N은 세준의 병사 수, M은 세비의 병사 수
    # 세준과 세비의 병사 내림차순 정렬
    sejun = sorted(list(map(int, input().split())), reverse=True)
    sebi = sorted(list(map(int, input().split())), reverse=True)
    
    while sejun and sebi:
        if sejun[0] >= sebi[0]: # 세준 병사의 힘이 세비 병사의 힘과 같거나 더 강한 경우
            sebi.pop() # 세비 병사 제거
        else: # 세비의 병사가 더 강한 경우
            sejun.pop() # 세준 병사 제거
    
    # 남은 병사 수 확인하여 결과 출력
    if sejun:
        print('S')
    elif sebi:
        print('B')
    else:
        print('C')