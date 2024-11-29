import sys
input = sys.stdin.readline

N = int(input().strip())
ropes = []

for _ in range(N):
    ropes.append(int(input().strip()))

ropes.sort(reverse=True)

max_weight = 0
for rope in range(N):
    weight = ropes[rope] * (rope + 1)
    max_weight = max(max_weight, weight)

print(max_weight)