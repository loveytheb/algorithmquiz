def solution(babbling):
    valid_words = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word
        for valid in valid_words:
            temp = temp.replace(valid, " ")
        # 남은 문자가 없으면 발음 가능한 단어
        if temp.strip() == "":
            count += 1

    return count
