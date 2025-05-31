function solution(x, y, n) {
    var answer = 0;
    let table = Array.from(new Array(y+1), ()=>-1);
    table[x] = 0
    for (let i=x; i<y+1; i++) {
        if (table[i]===-1) continue;
        if (i+n<=y) {
            if (table[i+n]!==-1) {
                table[i+n] = Math.min(table[i+n], table[i] + 1);
            } else {
                table[i+n] = table[i] + 1;
            }
        }
        if (i*2<=y) {
            if (table[i*2]!==-1) {
                table[i*2] = Math.min(table[i*2], table[i] + 1);
            } else {
                table[i*2] = table[i] + 1;
            }
        }
        if (i*3<=y) {
            if (table[i*3]!==-1) {
                table[i*3] = Math.min(table[i*3], table[i] + 1);
            } else {
                table[i*3] = table[i] + 1;
            }
        }
    }
    answer = table[y];
    return answer;
}