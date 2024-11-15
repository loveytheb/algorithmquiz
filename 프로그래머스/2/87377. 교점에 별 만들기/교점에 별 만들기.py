def solution(line):
    points = []
    n = len(line)
    
    # 교점 계산
    for i in range(n):
        for j in range(i + 1, n):
            # 계수 추출
            A1, B1, C1 = line[i]
            A2, B2, C2 = line[j]
            
            # 분모 계산
            denominator = A1 * B2 - A2 * B1
            if denominator == 0:  # 평행하거나 동일한 직선
                continue
            
            # x, y 계산을 위한 분자 계산
            x_numerator = B1 * C2 - B2 * C1
            y_numerator = A2 * C1 - A1 * C2
            # 정수 좌표 여부 확인
            if x_numerator % denominator != 0 or y_numerator % denominator != 0:
                continue
            
            # 정수 좌표 저장
            x = x_numerator // denominator
            y = y_numerator // denominator
            points.append((x, y))
    
    # # 교점이 없으면 빈 배열 반환
    # if not points:
    #     return []
    
    # 좌표 변환을 위한 최소/최대값 계산
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    
    # 결과 평면 크기 설정
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]
    
    # 별 찍기
    for x, y in points:
        transformed_x = x - min_x
        transformed_y = max_y - y
        grid[transformed_y][transformed_x] = '*'
    
    # 결과를 문자열 리스트로 반환
    return [''.join(row) for row in grid]
