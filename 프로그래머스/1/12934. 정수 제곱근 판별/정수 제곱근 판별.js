function solution(n) {
    var answer = -1;
    if (Math.round(n**0.5)===n**0.5) {
        answer = (n**0.5+1)**2
    }
    return answer;
}