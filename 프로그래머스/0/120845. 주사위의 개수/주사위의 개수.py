def solution(box, n):
    # 각 변의 길이를 주사위의 변의 길이로 나눈 몫을 구합니다.
    count_x = box[0] // n
    count_y = box[1] // n
    count_z = box[2] // n
    
    # 각 변에서 구할 수 있는 주사위 개수의 곱을 구합니다.
    total_count = count_x * count_y * count_z
    
    return total_count
