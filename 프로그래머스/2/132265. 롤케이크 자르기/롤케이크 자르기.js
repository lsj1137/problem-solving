function solution(topping) {
    var answer = 0;
    let leftKind = new Set();
    let rightCount = {};
    let rightKind = 0;
    for (top of topping) {
        if (rightCount[top]) {
            rightCount[top] += 1;
        } else {
            rightKind += 1;
            rightCount[top] = 1;
        }
    }
    for (top of topping) {
        rightCount[top] -= 1;
        if (rightCount[top] === 0) {
            rightKind -= 1;
        }
        leftKind.add(top);
        if (leftKind.size === rightKind) {
            answer += 1;
        }
    }
    return answer;
}
