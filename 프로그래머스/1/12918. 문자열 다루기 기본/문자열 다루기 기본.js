function solution(s) {
    var answer = true;
    if (s.length!==4 && s.length!==6) {
        answer = false;
    }
    if (s!=parseInt(s)) {
        answer = false;
    }
    return answer;
}