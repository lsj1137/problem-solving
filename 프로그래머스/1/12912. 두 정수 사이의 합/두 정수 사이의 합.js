function solution(a, b) {
    var answer = 0;
    let big = Math.max(a,b);
    let sml = Math.min(a,b);
    answer = big*(big+1)/2 - sml*(sml-1)/2;
    return answer;
}