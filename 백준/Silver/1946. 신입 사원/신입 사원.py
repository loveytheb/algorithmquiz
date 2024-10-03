import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

for _ in range(T):
    N = int(input()) # 지원자 수
    applicants = []
    
    for _ in range(N):
        paper, interview = map(int, input().split()) # 각 지원자의 서류와 면접 등수
        applicants.append((paper, interview))
      
    applicants.sort() # 서류 등수 기준 오름차순 정렬
    
    count = 1 # 서류 1등은 이미 뽑힌 것이나 마찬가지니까 초기값 1
    cut_line = applicants[0][1] # 서류 1등의 면접 점수가 기준
    
    for i in applicants[1:]: # 두 번째 지원자부터 비교
        # 서류 등수는 앞 사람보다 낮지만, 면접 등수가 앞 사람보다 높으면 합격
        if cut_line > i[1]: # 면접 등수가 더 작을 경우 합격
            count += 1
            cut_line = i[1]
         
    print(count)