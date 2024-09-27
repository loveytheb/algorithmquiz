import sys
input = sys.stdin.readline

L = int(input().strip())  # 문자열의 길이 입력
S = input().strip()       # 문자열 입력
result = 0

for i in range(len(S)):
    num = ord(S[i]) - 96
    result += num * (31 ** i)
    
print(result)