def solution(progresses, speeds):
    answer = []
    day = 0 # 배포 날짜
    count = 0 # 배포된 작업 개수
    
    while len(progresses) > 0:
        if progresses[0] + speeds[0] * day >= 100: # 작업의 진도가 100% 이상이면
            progresses.pop(0) # 작업 진도 리스트에서 제거
            speeds.pop(0) # 작업의 개발 속도 리스트에서 제거
            count += 1 # 배포된 작업 개수 +1
        else: # 작업의 진도 100% 안된다면
            if count > 0: # 배포할 작업이 있다면
                answer.append(count) # answer에 배포 개수 추가
                count = 0 # 배포된 작업 개수 초기화
            day += 1 # 다음 날짜로 넘어가야 하기 때문에 +1
    answer.append(count) # progresses가 0이 되면 while문 끝났기 때문에 밖에서 append
    return answer