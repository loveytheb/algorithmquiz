import sys
input = sys.stdin.readline

N = int(input())

for case_number in range(1, N + 1):
    words = input().strip().split()       # 공백 기준으로 단어 나눔
    reverse_words = words[::-1]   # 단어 리스트 뒤집기
    result = ' '.join(reverse_words)  # 뒤집힌 단어를 공백으로 합치기
    print(f"Case #{case_number}: {result}")