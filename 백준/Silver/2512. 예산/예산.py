import sys
input = sys.stdin.readline

N = int(input().strip()) # 지방 수
budgets = list(map(int, input().strip().split())) # 각 지방 예산 요청 list
M = int(input().strip()) # 총 예산

low, high = 0, max(budgets)

result = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(min(b, mid) for b in budgets)
    
    if total <= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(result)