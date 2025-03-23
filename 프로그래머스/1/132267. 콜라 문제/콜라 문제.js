function solution(a, b, n) {
    var answer = 0;
    let total = n;
    while (total>=a) {
        answer += Math.floor(total/a)*b;
        total = Math.floor(total/a)*b + total%a;
    }
    return answer;
}