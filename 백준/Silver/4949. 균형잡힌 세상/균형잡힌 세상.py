def isbalanced(line):
    stack = []
    for char in line:
        if char in '([':
            stack.append(char)  # 여는 괄호를 스택에 추가
        elif char in ')]':
            if not stack:  # 스택이 비어있는데 닫는 괄호가 오면 불균형
                return 'no'
            top = stack.pop()  # 스택에서 여는 괄호를 제거
            # 짝이 맞지 않으면 불균형
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return 'no'
    return 'yes' if not stack else 'no'  # 스택이 비어있으면 균형 잡힘

while True:
    line = input().rstrip()  # 입력 받기, 공백 제거
    if line == '.':
        break  # 종료 조건
    print(isbalanced(line))  # 각 줄에 대해 균형 여부 출력
