function sortTable(a,b,col) {
    if (a[col]!==b[col]) {
        return a[col] - b[col]
    } else {
        return b[0] - a[0]
    }
}

function solution(data, col, row_begin, row_end) {
    var answer = 0;
    let table = [...data];
    table.sort((a,b)=>sortTable(a,b,col-1));
    let sums = [];
    for (let i=row_begin; i<row_end+1; i++) {
        sums.push(table[i-1].reduce((acum, cur)=> acum+cur%i,0));
    }
    answer = sums.reduce((acum, cur)=> acum ^ cur, 0);
    return answer;
}