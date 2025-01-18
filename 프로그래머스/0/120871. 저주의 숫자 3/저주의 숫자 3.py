def solution(n):
    count = 0
    number = 0
    
    while count < n:
        number += 1
        if '3' in str(number) or number % 3 == 0:
            continue
        count += 1
    
    return number
