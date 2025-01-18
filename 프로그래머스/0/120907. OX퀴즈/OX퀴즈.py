def solution(quiz):
    result = []
    for q in quiz:
        expression, expected = q.split(' = ')
        if eval(expression) == int(expected):
            result.append("O")
        else:
            result.append("X")
    return result