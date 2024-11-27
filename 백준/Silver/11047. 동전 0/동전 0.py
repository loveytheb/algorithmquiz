import sys
input = sys.stdin.readline

# N: 동전 종류, K: 목표 금액
N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input().strip()))

# 큰 동전부터 사용하기 위함
coins.sort(reverse=True)

count = 0

for coin in coins:
    count += K // coin
    K %= coin

print(count)