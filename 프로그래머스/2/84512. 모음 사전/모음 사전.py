from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    combinations = []

    for length in range(0, 6):
        for combo in product(vowels, repeat=length):
            combinations.append(''.join(combo))

    combinations.sort()

    return combinations.index(word)