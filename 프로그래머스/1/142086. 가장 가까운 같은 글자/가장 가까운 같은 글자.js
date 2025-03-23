function solution(s) {
    var answer = [];
    let position = {};
    for (c in s) {
        if (position[s[c]]===0 || position[s[c]]){
            answer.push(parseInt(c)-position[s[c]]);
        } else {
            answer.push(-1);
        }
        position[s[c]] = parseInt(c);
    }
    return answer;
}