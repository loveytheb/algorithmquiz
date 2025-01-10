def solution(s, num1, num2):
    s_list = list(s) # 문자열을 리스트로 변환
    s_list[num1], s_list[num2] = s_list[num2], s_list[num1] # 인덱스 교환
    return ''.join(s_list) # 리스트를 문자열로 변환하여 반환
