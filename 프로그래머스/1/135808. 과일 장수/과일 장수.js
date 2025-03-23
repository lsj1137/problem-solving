function solution(k, m, score) {
    var answer = 0;
    let apples = score.sort();
    let count = 0
    for (let i=score.length-1; i>-1; i--) {
        count += 1;
        if (count%m === 0) {
            answer += apples[i]*m;
            count = 0;
        }
    }
    return answer;
}