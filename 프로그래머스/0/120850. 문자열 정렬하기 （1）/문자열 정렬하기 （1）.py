def solution(my_string):
    numbers = []
    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))
    numbers.sort()
    return numbers