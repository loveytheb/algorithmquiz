def solution(common):
    # 등차수열의 경우
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    # 등비수열의 경우
    else:
        return common[-1] * (common[1] // common[0])