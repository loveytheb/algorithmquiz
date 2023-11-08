// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
// -10,000 ≤ numbers의 원소 ≤ 10,000
// 1 ≤ numbers의 길이 ≤ 1,000

function solution(num) {
    const newNum = []
    for (let i = 0; i < num.length; i++) {
        // 1. i가 0부터 시작하고 num의 길이보다 작을 때 하나씩 증가하다가 num의 길이가 되면 멈추는 조건의 for문 만들기
        
        newNum.push(num[i] * 2);
        // 2. 새로운 배열인 newNum에 num의 안에 있는 i가 2배한 값을 push하기
    }
    // 3. i가 2배인 값들이 모인 newNum return하기
    return newNum;
}