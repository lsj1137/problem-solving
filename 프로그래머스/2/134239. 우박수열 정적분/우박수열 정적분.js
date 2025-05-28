function solution(k, ranges) {
    var answer = [];
    let curValue = k;
    let yValues = [curValue];
    while (curValue!==1) {
        if (curValue % 2 === 0) {
            curValue /= 2;
            yValues.push(curValue);
        } else {
            curValue *= 3;
            curValue += 1;
            yValues.push(curValue);
        }
    }
    let areas = [0];
    for (let i=0; i<yValues.length-1; i++) {
        areas.push((yValues[i] + yValues[i+1])/2);
        if (areas.length>1) {
            areas[areas.length-1] += areas[areas.length-2];
        }
    }
    for (r of ranges) {
        let start = r[0];
        let end = yValues.length+r[1]-1;
        if (start>end) {
            answer.push(-1);
        } else {
            answer.push(areas[end] - areas[start]);
        }
    }
    return answer;
}