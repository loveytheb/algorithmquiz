import sys
from collections import Counter

input = sys.stdin.readline

# 입력 처리
N = int(input().strip())
cards = list(map(int, input().strip().split()))
M = int(input().strip())
queries = list(map(int, input().strip().split()))

# Counter로 카드의 개수를 센다
count_cards = Counter(cards)

# 각 쿼리에 대해 해당 카드의 개수를 출력한다
result = [count_cards[query] for query in queries]
print(' '.join(map(str, result)))