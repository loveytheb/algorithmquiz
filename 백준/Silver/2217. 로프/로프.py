import sys
input = sys.stdin.readline

N = int(input().strip())
ropes = []

for _ in range(N):
    ropes.append(int(input().strip()))

# 가장 큰 중량 로프부터 사용
ropes.sort(reverse=True)

max_weight = 0
for rope in range(N):
    # rope + 1개 사용했을 때 최대중량
    weight = ropes[rope] * (rope + 1)
    max_weight = max(max_weight, weight)

print(max_weight)