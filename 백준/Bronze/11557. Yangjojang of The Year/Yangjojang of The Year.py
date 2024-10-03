import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 숫자

for _ in range(T):
    N = int(input()) # 참가하는 학교 수
    info = [] # 참가 학교 정보를 저장
    
    for _ in range(N):
        university, drinks = input().split() # 대학교 이름, 술의 양
        drinks = int(drinks) # 술의 양 정수로 변환
        info.append([drinks, university]) # 참가자 정보 리스트에 저장
        
    info.sort(reverse=True) # 술의 양을 기준으로 내림차순 정렬
    
    print(info[0][1]) # 가장 많은 술을 마신 대학교 이름 출력