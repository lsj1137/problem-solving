function solution(x, n) {
    var answer = [];
    for (let i=0; i<n; i++) {
        let N = 0;
        for (let j=0; j<i+1; j++) {
            N += x;
        }
        answer.push(N);
    }
    return answer;
}