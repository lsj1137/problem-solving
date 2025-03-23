function solution(numbers) {
    var answer = [];
    answer = new Array(numbers.length);
    answer[numbers.length-1] = -1;
    let maxStack = [-1];
    for (let i=numbers.length-1; i>0; i--) {
        if (numbers[i-1] >= numbers[i]) {
            while (maxStack.length>1 && numbers[i-1]>=maxStack[maxStack.length-1]) {
                maxStack.pop();
            }
        } else {
            maxStack.push(numbers[i]);
        }
        answer[i-1] = maxStack[maxStack.length-1];
    }
    return answer;
}