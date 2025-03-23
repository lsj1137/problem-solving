function solution(x) {
    var answer = true;
    let sum = [...x.toString()].reduce((a,v)=>a+=parseInt(v), 0);
    if (x%sum!==0) {
        answer = false;
    }
    return answer;
}