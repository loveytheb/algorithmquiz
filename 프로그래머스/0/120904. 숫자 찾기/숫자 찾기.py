def solution(num, k):
    index = str(num).find(str(k))
    if index != -1:
        return index + 1
    else:
        return -1