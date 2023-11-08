// 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
// 제한사항
// 0 < num1 ≤ 100
// 0 < num2 ≤ 100


function solution(num1, num2) {
    // 1. num1, num2 범위 정하기
    if (0 < num1 && num1 <= 100)
    if (0 < num2 && num2 <= 100)

    // 2. num1에서 num2를 나눈 나머지 값 return하기
    return Math.floor( num1 % num2);
};

console.log(solution(7, 5)); // 2