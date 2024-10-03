import sys
input = sys.stdin.readline

N = int(input()) # N개의 수
A = list(map(int, input().split())) # A 리스트
B = list(map(int, input().split())) # B 리스트

# A는 오름차순, B는 내림차순 정렬
A.sort()
B.sort(reverse=True)

result = 0 # 합계를 저장할 변수

# A와 B의 요소를 곱해서 합계 계산
for i in range(N):
    result += A[i] * B[i] # A의 i번째 요소와 B의 i번째 요소를 곱해 result에 더함
    
print(result)