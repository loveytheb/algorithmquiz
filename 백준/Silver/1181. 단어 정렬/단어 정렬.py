import sys
input = sys.stdin.readline

N = int(input()) # 단어의 개수

# N개의 단어를 입력받아 리스트에 저장
words = [str(input().strip()) for _ in range(N)] # 입력받은 단어에서 공백 제거 후 저장

words = list(set(words)) # 중복된 단어를 제거하기 위해 set으로 변환 후 다시 리스트로 변환

words.sort() # 단어를 사전 순으로 정렬
words.sort(key=len) # 단어를 길이 순으로 정렬 (길이가 짧은 것부터)

for word in words: # 정렬된 단어들을 출력
    print(word) # 각 단어를 한 줄씩 출력