def solution(my_string):
    total = 0
    for char in my_string:
        if char.isdigit():
            total += int(char)
    return total
