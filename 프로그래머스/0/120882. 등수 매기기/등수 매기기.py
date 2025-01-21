def solution(score):
    # 각 학생의 평균 점수와 원래 인덱스를 함께 저장
    averages = [(sum(s) / 2, i) for i, s in enumerate(score)]
    
    # 평균 점수를 기준으로 내림차순 정렬
    sorted_averages = sorted(averages, key=lambda x: -x[0])
    
    # 등수 리스트 초기화
    ranks = [0] * len(score)
    
    # 정렬된 평균 점수를 기반으로 등수 매기기
    rank = 1
    for i in range(len(sorted_averages)):
        # 첫 번째 학생이거나 이전 학생과 평균이 다를 때만 등수 갱신
        if i > 0 and sorted_averages[i][0] != sorted_averages[i-1][0]:
            rank = i + 1
        ranks[sorted_averages[i][1]] = rank
    
    return ranks
