function solution(s){
    var answer = true;
    let S = s.toLowerCase();
    let balance = 0;
    for (c of S) {
        if (c==='p') {
            balance += 1;
        } else if (c==='y') {
            balance -= 1;
        }
    }
    if (balance!==0) answer = false;
    return answer;
}