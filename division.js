// 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
// 제한사항
// 0 < num1 ≤ 100
// 0 < num2 ≤ 100

function solution(num1, num2) {
    // 1. num1, num2 범위 설정하기
    if(0 <= num1 && num1 <= 100)
    if(0 <= num2 && num2 <= 100)

    // 2. num1을 num2로 나누기 
    var answer = num1 / num2;

    // 3. 나눈 값에 1,000을 곱한 후 정수 부분 return하도록 하기
    return Math.floor(answer * 1000);
};

console.log(solution(3, 2)); // 1500
