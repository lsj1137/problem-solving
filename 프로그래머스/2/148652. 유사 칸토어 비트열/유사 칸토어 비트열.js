function divideConquer(n, l, r) {
    let answer = 0;
    let unit = 5**(n-1);
    for (let i=0; i<5; i++) {
        let rangeSt = unit*i;
        let rangeFn = unit*(i+1)-1;
        if (i===2) {
            continue;
        }
        if (rangeSt < l && l <= rangeFn) {
            answer += divideConquer(n-1, l%unit, Math.min(rangeFn, r)%unit);
        } else if (l <= rangeSt && rangeFn <= r) {
            if (i!==2) {
                answer += 4**(n-1);
            }
        } else if (rangeSt <= r && r <= rangeFn) {
            answer += divideConquer(n-1, Math.max(l, rangeSt)%unit, r%unit);
        }
    }
    return answer;
}

function solution(n, l, r) {
    var answer = 0;
    answer = divideConquer(n, l-1, r-1);
    return answer;
}