def is_good_word(word):
    stack = []
    
    for char in word:
        if stack and stack[-1] == char:  # 스택의 마지막 문자와 현재 문자가 같으면
            stack.pop()  # 짝이 맞으므로 스택에서 제거
        else:
            stack.append(char)  # 짝이 아니면 스택에 추가
    
    return len(stack) == 0  # 스택이 비었으면 좋은 단어

# 입력 처리
n = int(input())  # 단어의 개수 입력 받기
count = 0  # 좋은 단어의 개수를 셀 변수

for _ in range(n):
    word = input().strip()
    if is_good_word(word):
        count += 1

print(count)  # 좋은 단어의 개수 출력