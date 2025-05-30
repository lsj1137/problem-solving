function solution(topping) {
    var answer = 0;
    let leftKind = new Set();
    let rightKind = {};
    let totalKind = 0;
    for (top of topping) {
        if (rightKind[top]) {
            rightKind[top] += 1;
        } else {
            totalKind += 1;
            rightKind[top] = 1;
        }
    }
    for (top of topping) {
        rightKind[top] -= 1;
        if (rightKind[top] === 0) {
            totalKind -= 1;
        }
        leftKind.add(top);
        if (leftKind.size === totalKind) {
            answer += 1;
        }
    }
    return answer;
}