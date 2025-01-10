def solution(my_string):
    seen = set()
    result = []
    for char in my_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
