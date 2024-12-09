import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip()) # 상근이가 가지고 있는 카드 개수
cards = list(map(int, input().strip().split())) # 상근이가 가지고 있는 카드 종류
M = int(input().strip()) # 상근이가 몇 개 가지고 있는 카드인지 구해야 할 개수
queries = list(map(int, input().strip().split())) # 확인할 카드 목록

count_cards = defaultdict(int)
for card in cards:
    count_cards[card] += 1

result = []
for query in queries:
    count = count_cards[query] # 해당 쿼리 카드 개수
    result.append(count)

print(' '.join(map(str, result)))