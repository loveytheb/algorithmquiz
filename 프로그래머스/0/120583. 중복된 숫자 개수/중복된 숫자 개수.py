def solution(array, n):
    result = []
    for i in array:
        if i == n:
            result.append(i)
    return len(result)