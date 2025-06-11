function solution(citations) {
    var answer = 0;
    citations.sort((a,b)=>b-a);
    let i = 0;
    answer = citations[0];
    let moreOrSame = 1;
    while (moreOrSame < answer) {
        answer -= 1;
        if (answer <= citations[i+1]) {
            i += 1;
            moreOrSame += 1;
        }
    }
    return answer;
}