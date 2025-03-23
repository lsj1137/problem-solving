function solution(s) {
    var answer = 0;
    let start = s[0];
    let sameLen = 0;
    for (c of s) {
        if (sameLen === 0) {
            start = c;
            answer += 1;
        }
        if (c === start) {
            sameLen += 1;
        } else {
            sameLen -= 1;
        }
    }
    return answer;
}