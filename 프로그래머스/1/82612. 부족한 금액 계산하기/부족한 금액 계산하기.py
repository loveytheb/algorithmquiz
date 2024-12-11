def solution(price, money, count):
    total_cost = sum(price * i for i in range(1, count + 1))
    
    result = total_cost - money
    
    return max(result, 0)