function solution(n, left, right) {
    var answer = [];
    let leftP = [Math.floor(left/n), left%n];
    let rightP = [Math.floor(right/n), right%n];
    let curP = [...leftP];
    while (curP[0]!==rightP[0] || curP[1]!==rightP[1]) {
        answer.push(Math.max(...curP) + 1);
        curP[1] += 1;
        if (curP[1] > n-1) {
            curP[0] += 1;
            curP[1] = 0;
        }
    }   
    answer.push(Math.max(...curP) + 1);
    return answer;
}