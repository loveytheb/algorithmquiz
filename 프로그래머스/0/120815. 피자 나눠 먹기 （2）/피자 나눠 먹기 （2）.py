def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n):
    pizza_slices = 6
    return lcm(n, pizza_slices) // pizza_slices
