import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)] # N개의 문자열을 입력 받아 words 리스트에 저장

for word in words:
    if word[::-1] in words: # 뒤집은 문자열이 리스트에 존재하는지 확인
        word_length = len(word)
        print(word_length, word[word_length // 2]) # 가운데 문자 출력
        break
