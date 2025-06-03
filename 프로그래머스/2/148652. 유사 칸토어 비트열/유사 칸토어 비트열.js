function divideConquer(n, l, r) {
    let answer = 0;
    let unit = 5**(n-1);
    // console.log(n,l,r);
    for (let i=0; i<5; i++) {
        let rangeSt = unit*i;
        let rangeFn = unit*(i+1)-1;
        if (i===2) {
            continue;
        }
        if (rangeSt < l && l <= rangeFn) {
            // console.log("?", rangeSt, l, rangeFn);
            answer += divideConquer(n-1, l%unit, Math.min(rangeFn, r)%unit);
        } else if (l <= rangeSt && rangeFn <= r) {
            if (i!==2) {
                answer += 4**(n-1);
            }
        } else if (rangeSt <= r && r <= rangeFn) {
            // console.log("!", rangeSt, r, rangeFn);
            answer += divideConquer(n-1, Math.max(l, rangeSt)%unit, r%unit);
        }
    }
    // console.log(answer);
    // console.log("-----");
    return answer;
}

function solution(n, l, r) {
    var answer = 0;
    answer = divideConquer(n, l-1, r-1);
    return answer;
}

// 4 30 118 => 39
// 3 1 125 => 64
// 4 27 68 => 15