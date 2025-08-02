function solution(land) {
    var answer = 0;
    let scores = [[0,-1],[0,-1],[0,-1],[0,-1]];
    for (line of land) {
        let nextScores = line.map((score, index)=> [score,index]);
        scores.sort((a,b)=>b[0]-a[0]);
        for (ns of nextScores) {
            let i=0;
            while (scores[i][1] === ns[1]) {
                i += 1;
            }
            ns[0] += scores[i][0];
        }
        scores = nextScores;
    }
    answer = Math.max(...scores.map((arr)=>arr[0]));
    return answer;
}