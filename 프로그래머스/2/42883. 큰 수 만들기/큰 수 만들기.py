def solution(number, k):
    stack = []
    
    for num in number:
        # 아직 제거할 숫자 남아 있고, stack 비어있지 않고, stack의 마지막 숫자가 현재 숫자보다 작으면
        while k > 0 and stack and stack[-1] < num:
            stack.pop() # stack 마지막 숫자 제거
            k -= 1 # 제거할 숫자 개수 -1
        stack.append(num) # 현재 숫자 stack에 추가
    
    # 아직 제거하지 못한 숫자가 남아있을 경우 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)

