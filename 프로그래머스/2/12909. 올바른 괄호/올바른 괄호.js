function solution(s){
    var answer = true;
    let stack = [];
    for (c of s) {
        if (c==='\(') {
            stack.push('\(');
        } else {
            if (stack.length===0) {
                answer = false;
                break;
            } else {
                stack.pop();
            }
        }
    }
    if (stack.length>0) {
        answer = false;
    }
    return answer;
}