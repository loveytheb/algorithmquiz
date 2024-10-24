def solution(brown, yellow):
    total = brown + yellow # 전체 면적
    
    for height in range(3, total + 1): # 세로 길이 3 이상, 전체 면적 초과 안됨
        if total % height == 0: # height가 total의 약수이면
            width = total // height # width 계산
            
            if (width - 2) * (height - 2) == yellow: # 노란색 카펫 면적이 yellow와 같으면
                return [width, height] # 반환