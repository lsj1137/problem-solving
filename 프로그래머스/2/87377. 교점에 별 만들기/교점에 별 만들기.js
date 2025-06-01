function isParallel(A,B,E, C,D,F) {
    return A*D === B*C;
}

function getMeet(A,B,E, C,D,F) {
    return [(B*F-E*D) / (A*D-B*C), (E*C-A*F) / (A*D-B*C)]
}

function solution(line) {
    var answer = [];
    let stars = [];
    let start = [Infinity,Infinity];
    let end = [-Infinity, -Infinity];
    for (let i=0; i<line.length-1; i++) {
        for (let j=i+1; j<line.length; j++) {
            if (isParallel(...line[i], ...line[j])) continue;
            let [x,y] = getMeet(...line[i], ...line[j]);
            if (Number.isInteger(x) && Number.isInteger(y)) {
                if (y<start[0]) {
                    start[0] = y;
                }
                if (x<start[1]) {
                    start[1] = x;
                }
                if (y>end[0]) {
                    end[0] = y;
                }
                if (x>end[1]) {
                    end[1] = x;
                }
                stars.push([y,x]);
            }
        }
    }
    const starSet = new Set(stars.map(([x, y]) => `${x},${y}`));
    for (let i=end[0]; i>start[0]-1; i--) {
        let line = '';
        for (let j=start[1]; j<end[1]+1; j++) {
            if (starSet.has(`${i},${j}`)) {
                line += '*';
            } else {
                line += '.'
            }
        }
        answer.push(line);
    }
    return answer;
}