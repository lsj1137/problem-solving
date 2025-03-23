function solution(n) {
    var answer = 0;
    let [n0, n1] = [n, '',''];
    while (n0/3 > 0) {
        n1 = (n0%3).toString() + n1;
        n0 = Math.floor(n0/3);
    }
    for (let i=0; i<n1.length; i++) {
        answer += n1[i] * (3**i);
    }
    return answer;
}