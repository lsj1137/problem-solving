function solution(n, words) {
    var answer = [];
    let done = {};
    let turn = 1;
    let index = 0;
    for (let i=0;i<words.length; i++) {
        let w = words[i];
        if (done[w] !== undefined) {
            answer = [index+1, turn];
            break;
        } else if (i>0 && w[0]!==words[i-1][words[i-1].length-1]) {
            answer = [index+1, turn];
            break;
        } else {
            done[w] = [index+1, turn];
        }
        index = (index + 1) % n;
        if (index===0) {
            turn += 1;
        }
    }
    if (answer.length===0) {
        answer = [0,0];
    }
    return answer;
}