def solution(arr, n):
    result = []
    
    for i in range(0, len(arr), n):
        result.append(arr[i:i+n])
    
    return result
