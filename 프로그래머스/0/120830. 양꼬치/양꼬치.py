def solution(n, k):
    freeK = (n // 10) * 2000 
    return (n * 12000) + (k * 2000 - freeK)