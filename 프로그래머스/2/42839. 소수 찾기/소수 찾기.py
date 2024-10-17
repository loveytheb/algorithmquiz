from itertools import permutations

def is_prime(n):
    if n < 2: # 2보다 작으면 소수 아님
        return False
    for i in range(2, int(n ** 0.5) + 1): # 약수로 나누어지면 소수 아님
        if n % i == 0:
            return False
    return True # 그 외의 경우는 소수
        

def solution(numbers):
    prime_numbers = set() # 중복 제외하고 소수 저장
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i) # 모든 순열 생성
    
        for perm in perms:
            num = int(''.join(perm)) # 정수로 변환
            if is_prime(num): # 변환된 정수가 소수인지 확인
                prime_numbers.add(num) # 소수이면 추가
    
    return len(prime_numbers)