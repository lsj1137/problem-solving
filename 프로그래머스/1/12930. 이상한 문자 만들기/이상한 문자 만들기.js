function solution(s) {
    var answer = '';
    let index = 0;
    for (c of s) {
        if (c===' '){
            index = 0;
            answer += c;
            continue;
        }
        if (index%2 === 0) {
            answer += c.toUpperCase();
        } else {
            answer += c.toLowerCase();
        }
        index += 1;
    }
    return answer;
}