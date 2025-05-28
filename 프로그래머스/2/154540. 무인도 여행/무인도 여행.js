function dfs(x,y,check, maps, food) {
    check[x][y] = true;
    let result = food;
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    for (let i=0; i<4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (nx>-1 && ny>-1 && nx<maps.length && ny<maps[0].length && !check[nx][ny] && maps[nx][ny]!=='X') {
            result = dfs(nx, ny, check, maps, result + Number(maps[nx][ny]));
        }
    }
    return result;
}

function solution(maps) {
    var answer = [];
    let check = Array.from(new Array(maps.length), ()=>Array.from(new Array(maps[0].length), ()=>false));
    for (let i=0; i<check.length; i++) {
        for (let j=0; j<check[0].length; j++) {
            if (check[i][j] || maps[i][j] === 'X') continue;
            answer.push(dfs(i,j,check,maps, Number(maps[i][j])));
        }
    }
    answer.sort((a,b)=>a-b);
    if (answer.length===0) {
        answer.push(-1);
    }
    return answer;
}