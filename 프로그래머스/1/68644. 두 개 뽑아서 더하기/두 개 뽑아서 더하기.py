def solution(numbers):
    result = set()
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            result.add(numbers[i] + numbers[j])

    return sorted(result)