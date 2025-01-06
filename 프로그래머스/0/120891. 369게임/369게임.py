def solution(order):
    count = 0
    for digit in str(order):
        if digit in '369':
            count += 1
    return count
