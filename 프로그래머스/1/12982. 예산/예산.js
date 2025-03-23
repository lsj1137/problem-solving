function solution(d, budget) {
    var answer = 0;
    d.sort((a,b)=>{
        if(a>b) {
            return 1;
        } else {
            return -1;
        }
    })
    for (p of d) {
        if (budget>=p) {
            budget -= p;
            answer += 1;
        } else {
            break;
        }
    }
    return answer;
}