def solution(a, b):
    i = str(a) + str(b)
    j = str(b) + str(a)
    
    if i == j:
        return int(i)
    else:
        return int(max(i, j))