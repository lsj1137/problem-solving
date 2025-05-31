function solution(weights) {
    var answer = 0;
    let sortedWeights = [...weights];
    sortedWeights.sort((a,b)=> a-b);
    let wCount = {};
    for (w of sortedWeights) {
        if (wCount[w]) {
            wCount[w] += 1;
        } else {
            wCount[w] = 1;
        }
    }
    while (sortedWeights.length>0) {
        let finding = sortedWeights.shift();
        wCount[finding] -= 1;
        let findings = [finding, finding*1.5, finding*2, finding*4/3];
        for (f of findings) {
            if (wCount[f]){
                answer += wCount[f];
            }
        }
    }
    return answer;
}