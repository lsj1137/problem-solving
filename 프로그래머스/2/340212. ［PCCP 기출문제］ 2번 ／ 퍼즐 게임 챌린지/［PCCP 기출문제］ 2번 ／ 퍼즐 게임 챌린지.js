function calCost (level, diffs, times) {
    let cost = 0;
    for (let i=0; i<times.length; i++) {
        cost += times[i];
        if (diffs[i] - level > 0) {
            cost += (times[i]+times[i-1]) * (diffs[i]-level)
        }
    }
    return cost
}

function solution(diffs, times, limit) {
    var answer = 0;
    let start = 0;
    let end = 100000;
    answer = Math.floor((start+end)/2);
    while (start<answer && answer<end) {
        if (calCost(answer, diffs, times) > limit) {
            start = answer;
        } else {
            end = answer;
        }
        answer = Math.floor((start+end)/2);
    }
    answer += 1;
    return answer;
}