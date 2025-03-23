function solution(left, right) {
    var answer = 0;
    let dict = {};
    for (let i=1; i<35; i++) {
        let j=1;
        while (i*j<=1000) {
            if (dict[i*j]) {
                dict[i*j].add(j);
                dict[i*j].add(i);
            } else {
                dict[i*j] = new Set([i,j]);
            }
            j+=1;
        }
    }
    for (let i=left; i<right+1; i++) {
        let arr = [...dict[i]];
        if (arr.length%2===0) {
            answer += i;
        } else {
            answer -= i;
        }
    }
    return answer;
}