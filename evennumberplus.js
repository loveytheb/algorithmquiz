// 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
// 0 < n ≤ 1000

function solution(n) {
    let answer = 0;

    for (let i = 0; i <= n; i++) {
        // 1. i가 0부터 시작하고 하나씩 증가할 때 n을 실행하면 멈춰라
        if (i % 2 === 0) {
            // 2. i를 2로 나눴을 때 나머지가 0인 경우 > 짝수
            answer += i;
            // 3. answer에 맞는 값인 i를 하나씩 더해라
        }
    }
    return answer;
}