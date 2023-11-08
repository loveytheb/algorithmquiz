// 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
// 제한사항
// -50000 ≤ num1 ≤ 50000
// -50000 ≤ num2 ≤ 50000

function solution(num1, num2) {
    // 1. num1과 num2의 범위 정하기
    if (-50000 <= num1 && num1 <= 50000)
    if (-50000 <= num2 && num2 <= 50000)
    // 2. num1에서 num2 차 return 하도록 만들기
    return num1 - num2;
}

console.log(solution(5, 1)); // 4