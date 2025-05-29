function solution(queue1, queue2) {
    var answer = 0;
    let longQue = [...queue1, ...queue2];
    let start = 0;
    let end = queue1.length-1;
    let sumQue1 = queue1.reduce((cur, acum)=>cur+acum, 0);
    let sumQue2 = queue2.reduce((cur, acum)=>cur+acum, 0);
    let goal = (sumQue1 + sumQue2)/2;
    console.log(goal);
    if ((sumQue1 + sumQue2)%2 !== 0) {
        return -1;
    }
    while (sumQue1!==goal) {
        if (sumQue1<goal) {
            if (end===longQue.length-1) {
                answer = -1;
                break;   
            }
            end += 1;
            sumQue1 += longQue[end];
        } else {
            if (start===end) {
                answer = -1;
                break;
            }
            sumQue1 -= longQue[start];
            start += 1;
        }
        answer += 1;
    }
    return answer;
}