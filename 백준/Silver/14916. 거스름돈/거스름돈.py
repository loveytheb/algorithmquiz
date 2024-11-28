import sys
input = sys.stdin.readline

n = int(input().strip())

def min_coins(n):
    count = 0
    
    while n > 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 2
        count += 1
    
    if n == 0:
        return count
    else:
        return -1

print(min_coins(n))