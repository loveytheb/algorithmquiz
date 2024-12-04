import sys
input = sys.stdin.readline

N = int(input().strip())

change = 1000 - N

coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += change // coin
    change %= coin

print(count)