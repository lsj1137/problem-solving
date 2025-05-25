function solution(info, n, m) {
    var answer = 0;
    let sortedInfo = info.sort((a,b) => {
        return b[0]/b[1] - a[0]/a[1];
    });
    console.log(sortedInfo);
    let [aLimit, bLimit] = [n, m]
    for (info of sortedInfo) {
        if (info[1] < bLimit) {
            bLimit -= info[1];
            sortedInfo = sortedInfo.filter((i)=>i!==info);
        } else {
            continue;
        }
    }
    let aList = sortedInfo.map((i)=>i[0]);
    let aSum = aList.reduce((cur, accum)=>cur+accum, 0);
    if (aSum < aLimit){
        answer = aSum;
    } else {
        answer = -1;
    }
    return answer;
}