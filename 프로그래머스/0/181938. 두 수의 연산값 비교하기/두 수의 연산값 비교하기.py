def solution(a, b):
    i = int(str(a) + str(b))
    j = 2 * a * b
    
    if i == j :
        return i
    else :
        return max(i, j)