function change(num, system) {
    let result = [];
    while (num>0) {
        let char = num % system;
        if (char === 10) {
            result.push('A');
        } else if (char === 11) {
            result.push('B');
        } else if (char === 12) {
            result.push('C');
        } else if (char === 13) {
            result.push('D');
        } else if (char === 14) {
            result.push('E');
        } else if (char === 15) {
            result.push('F');
        } else {
            result.push(char);
        }
        num = Math.floor(num / system);
    }
    if (result.length===0) {
        result.push('0');
    }
    let resultStr = result.reduce((acum, cur)=>cur + acum, '');
    return resultStr;
}

function solution(n, t, m, p) {
    var answer = '';
    let totalLen = t*m;
    let curLen = 0;
    let num = 0;
    let totalStr = '';
    while (curLen<totalLen) {
        let converted = change(num, n);
        totalStr += converted;
        curLen += converted.length;
        num += 1;
    }
    let myTurn = [p-1];
    for (let i=0; i<t-1; i++) {
        myTurn.push(myTurn[myTurn.length-1] + m);
    }
    for (turn of myTurn) {
        answer += totalStr[turn]
    }
    return answer;
}