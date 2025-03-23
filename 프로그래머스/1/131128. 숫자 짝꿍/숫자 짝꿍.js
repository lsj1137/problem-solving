function solution(X, Y) {
    let answer = '';
    let xCount = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0};
    let yCount = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0};
    for (char of X) {
        xCount[char] += 1;
    }
    for (char of Y) {
        yCount[char] += 1;
    }
    let isNotZero = false;
    for (let i=9; i>-1; i--) {
        if (i !== 0 && xCount[i] !== 0 && yCount[i] !==0) {
            isNotZero = true;
        }
        for (let j=0; j<Math.min(xCount[i], yCount[i]); j++) {
            answer += `${i}`;
        }
    }
    if (!answer) {
        answer = '-1';
    } else if (!isNotZero) {
        answer = '0'
    }
    return answer;
}