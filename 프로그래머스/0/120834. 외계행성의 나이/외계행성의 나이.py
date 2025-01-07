def solution(age):
    # 숫자 0-9를 알파벳 'a'-'j'로 변환
    num_to_char = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    
    result = ''
    for digit in str(age):
        char = num_to_char[digit]
        
        result += char
        
    return result