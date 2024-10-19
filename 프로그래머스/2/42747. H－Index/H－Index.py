def solution(citations):
    citations.sort(reverse=True) # 내림차순 정렬
    answer = 0
    
    for citation in citations:
        if citation >= answer + 1:
            answer += 1
        else:
            break
            
    return answer