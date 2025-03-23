function calDiv () {
    let dict = {};
    for (let i=1; i<317; i++) {
        let j=1;
        while (i*j<=100000) {
            if (dict[i*j]) {
                dict[i*j].add(j);
                dict[i*j].add(i);
            } else {
                dict[i*j] = new Set([i,j]);
            }
            j+=1;
        }
    }
    return dict
}

function solution(number, limit, power) {
    var answer = 0;
    let dict = calDiv();
    for (let i=1; i<number+1; i++) {
        let atk = [...dict[i]].length;
        if (atk>limit) {
            answer += power;
        } else {
            answer += atk;
        }
    }
    return answer;
}