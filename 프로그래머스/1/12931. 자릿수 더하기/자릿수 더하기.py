def solution(n):
    n_str = str(n)
    
    total_sum = 0
    
    for digit in n_str:
        digit_int = int(digit)
        
        total_sum += digit_int

    return total_sum