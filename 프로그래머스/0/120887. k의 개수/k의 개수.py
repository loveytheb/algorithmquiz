def solution(i, j, k):
    count = 0
    for num in range(i, j + 1):
        for digit in str(num):
            if digit == str(k):
                count += 1
        
    return count