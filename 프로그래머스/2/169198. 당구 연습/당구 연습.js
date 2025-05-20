function solution(m, n, startX, startY, balls) {
    var answer = [];
    let startPoints = [];
    let corners = [[0,0], [0,m], [n,0], [n,m]];
    startPoints.push([-startX, startY]);
    startPoints.push([m*2 - startX, startY]);
    startPoints.push([startX, -startY]);
    startPoints.push([startX, n*2 - startY]);
    for (ball of balls) {
        let curMin = (m*2) ** 2 + (n*2) ** 2;
        for (sp of startPoints) {
            if (sp[1] === startY && ball[1] === startY) {
                if (ball[0] > Math.min(sp[0], startX) && ball[0] < Math.max(sp[0], startX)) {
                    continue;
                }
            } else if (sp[0] === startX && ball[0] === startX) {
                if (ball[1] > Math.min(sp[1], startY) && ball[1] < Math.max(sp[1], startY)) {
                    continue;
                }
            }
            let dist = (ball[0]-sp[0])**2 + (ball[1]-sp[1])**2;
            curMin = Math.min(dist, curMin);
        }
        answer.push(curMin)
    }
    return answer;
}