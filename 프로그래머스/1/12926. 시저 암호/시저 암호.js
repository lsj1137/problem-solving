function change (code, n) {
    let result = code;
    result += n;
    if (code>=65 && code<=90 && result > 90) {
        result -= 26;
    } else if (code>=97 && code<=122 && result > 122) {
        result -= 26;
    }
    return result;
}

function solution(s, n) {
    var answer = '';
    for (c of s) {
        if (c===' ') {
            answer+=c;
            continue;
        }
        let newc = '';
        let oldCode = c.charCodeAt();
        let newCode = change(oldCode, n);
        answer += String.fromCharCode(newCode);
    }
    return answer;
}