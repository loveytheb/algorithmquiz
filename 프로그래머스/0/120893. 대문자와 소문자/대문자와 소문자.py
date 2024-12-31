def solution(my_string):
    result = []
    for char in my_string:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
    return ''.join(result)
