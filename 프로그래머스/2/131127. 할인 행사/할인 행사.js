function check(arr) {
    return arr.filter((n)=> n>0).length===0;
}

function solution(want, number, discount) {
    var answer = 0;
    let count = {};
    for (let i=0; i<want.length; i++) {
        count[want[i]] = number[i];
    }
    for (let i=0; i<10; i++) {
        if (count[discount[i]] !== undefined) {
            count[discount[i]] -= 1;
        }
    }
    if (check(Object.values(count))) {
        answer += 1;
    }
    for (let i=0; i<discount.length-10; i++) {
        let cant = discount[i];
        let can = discount[i+10];
        if (count[cant] !== undefined) {
            count[cant] += 1;
        }
        if (count[can] !== undefined) {
            count[can] -= 1; 
        }
        if (check(Object.values(count))) {
            answer += 1;
        }
    }
    return answer;
}