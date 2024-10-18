from collections import defaultdict

def solution(clothes):
    clothes_count = defaultdict(int)
    
    for _, category in clothes:
        clothes_count[category] += 1
    
    answer = 1
    for count in clothes_count.values() :
        answer *= (count + 1)
    
    return answer - 1