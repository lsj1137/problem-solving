function solution(ingredient) {
    var answer = 0;
    let stack = [];
    for (let i=0; i<ingredient.length; i++) {
        stack.push(ingredient[i]);
        if (stack.length>=4 && stack[stack.length-4].toString()+stack[stack.length-3].toString()+stack[stack.length-2].toString()+stack[stack.length-1].toString() === '1231') {
            stack.pop();
            stack.pop();
            stack.pop();
            stack.pop();
            answer+=1;
        }
    }
    return answer;
}