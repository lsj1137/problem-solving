function solution(t, p) {
    var answer = 0;
    let arr = [...t];
    let compare = [...t].splice(0,p.length);
    for (let i=p.length; i<t.length; i++) {
        if (compare.join('') <= p) {
            answer += 1;
        }
        compare.shift();
        compare.push(arr[i]);
    }
    if (compare.join('') <= p) {
        answer += 1;
    }
    return answer;
}