function solution(k, score) {
    var answer = [];
    let curRank = [];
    for (s in score) {
        if (s<k || (s>=k && score[s] > curRank[0])) {
            curRank.push(score[s]);
        }
        curRank.sort((a,b)=>{
            if (a>b) {
                return 1;
            } else {
                return -1;
            }
        });
        if (curRank.length>k) {
            curRank.shift();
        }
        answer.push(curRank[0]);
    }
    return answer;
}