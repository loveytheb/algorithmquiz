def solution(array, n):
    result = []
    for char in array:
        result.append(abs(n - char))
    
    min_result = min(result)  # 가장 작은 차이 값 찾기
    closest_numbers = []
    
    for i in range(len(result)):
        if result[i] == min_result:
            closest_numbers.append(array[i])
    
    return min(closest_numbers)
