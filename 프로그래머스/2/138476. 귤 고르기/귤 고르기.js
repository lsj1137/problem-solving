function solution(k, tangerine) {
    var answer = 0;
    let division = {};
    for (t of tangerine) {
        if (division[t]) {
            division[t] += 1;
        } else {
            division[t] = 1;
        }
    }
    let divisionList = Object.entries(division);
    divisionList.sort((a,b)=>b[1]-a[1]);
    for (div of divisionList) {
        answer += 1;
        k -= div[1];
        if (k<=0) {
            break;
        }
    }
    return answer;
}