function solution(n, lost, reserve) {
    var answer = 0;
    
    // lost, reserve 배열 정렬
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
            
    // 도난 당하지 않은 학생 수 구학;
    answer = n - lost.length;
        
    // 여벌 체육복 있지만 도난 당한 학생 => 체육복 빌려줄 수 없음
    for (let i = 0; i < lost.length; i++) {
        for (let j = 0; j < reserve.length; j++) {
            if (lost[i] === reserve[j]) {
                answer++;
                lost[i] = - 1;
                reserve[j] = -1;
                break;
            }
        }
    }
    
    // 도난 당했지만 체육복 빌릴 수 있는 학생
    for (let i = 0; i < lost.length; i++) {
        for (let j = 0; j < reserve.length; j++) {
            if (lost[i] - 1 === reserve[j] || lost[i] + 1 === reserve[j]) {
                answer++;
                reserve[j] = -1;
                break;
            }
        }
    }    
    return answer;
}