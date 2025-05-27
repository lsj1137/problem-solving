function solution(k, d) {
    var answer = 0;
    for (let x=0; x<=d; x+=k) {
        let y = (d**2 - x**2)**0.5;
        answer += Math.floor(Math.floor(y)/k) + 1;
    }
    return answer;
}