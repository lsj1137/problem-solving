function solution(num) {
    var answer = 0;
    let target = num;
    while (answer<=500 && target!==1) {
        if (target%2===0) {
            target/=2;
        } else {
            target*=3;
            target+=1;
        }
        answer += 1;
    }
    if (target!==1) {
        answer = -1
    }
    return answer;
}