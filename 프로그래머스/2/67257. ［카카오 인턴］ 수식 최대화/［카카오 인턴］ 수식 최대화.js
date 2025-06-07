function add (a,b) {
    return Number(a)+Number(b);
}

function sub (a,b) {
    return Number(a)-Number(b);
}

function mul (a,b) {
    return Number(a)*Number(b);
}

function solution(expression) {
    var answer = 0;
    let order = ['+-*','+*-','-+*','-*+','*+-','*-+'];
    let expArr = [];
    let n = '';
    for (let i=0; i<expression.length; i++) {
        if (expression[i] !== '+' && expression[i] !== '-' && expression[i] !== '*') {
            n += expression[i];
        } else {
            expArr.push(n);
            expArr.push(expression[i]);
            n = '';
        }
    }
    expArr.push(n);
    let results = [];
    for (o of order) {
        let copyArr = [...expArr];
        for (operator of o) {
            for (let i=0; i<copyArr.length; i++) {
                let operand = 0;
                if (copyArr[i] === operator) {
                    if (operator==='+') {
                        operand = add(copyArr[i-1], copyArr[i+1]);
                    } else if (operator==='-') {
                        operand = sub(copyArr[i-1], copyArr[i+1]);
                    } else {
                        operand = mul(copyArr[i-1], copyArr[i+1]);
                    }
                    copyArr[i-1] = '';
                    copyArr[i] = '';
                    copyArr[i+1] = operand;
                }
            }
            copyArr = copyArr.filter((n)=>n!=='');
        }
        results.push(copyArr[0]);
    }
    results.sort((a,b)=>a-b);
    answer = Math.max(-results[0], results[results.length-1])
    return answer;
}