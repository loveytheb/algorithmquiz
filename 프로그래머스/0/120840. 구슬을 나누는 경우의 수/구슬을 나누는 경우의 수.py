import math

def solution(balls, share):
    # balls개의 구슬 중 share개를 선택하는 경우의 수를 계산
    return math.comb(balls, share)
