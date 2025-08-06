function getGD(n){
    if (n===1) {
        return 0;
    }
    let result = 1;
    for (let i=2; i<=n**0.5; i++) {
        if (n%i===0) {
            let c = i;
            if (n/i<=10000000) {
                result = n/i;
                break;
            }
            result = result > c ? result:c;
        }
    }
    return result;
}

function solution(begin, end) {
    var answer = [];
    for (let i=begin; i<end+1; i++) {
        answer.push(getGD(i));
    }
    return answer;
}