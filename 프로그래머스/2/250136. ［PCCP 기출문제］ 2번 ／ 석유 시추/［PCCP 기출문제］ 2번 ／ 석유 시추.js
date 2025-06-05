function dfs(x, y, land, check, areaNum) {
    let stack = [[x, y]];
    check[x][y] = true;
    land[x][y] = areaNum;
    let result = 1;
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    while (stack.length>0) {
        const [cx, cy] = stack.pop();
        for (let i=0; i<4; i++) {
            let nx = cx + dx[i];
            let ny = cy + dy[i];
            if (nx>-1 && ny>-1 && nx<land.length && ny<land[0].length && !check[nx][ny] && land[nx][ny]===1) {
                check[nx][ny] = true;
                land[nx][ny] = areaNum;
                stack.push([nx, ny]);
                result++;
            }
        }
    }
    return result;
}

function solution(land) {
    var answer = 0;
    let check = Array.from(new Array(land.length), ()=> Array.from(new Array(land[0].length), ()=>false));
    let area = {};
    let areaNum = 1;
    for (let i=0; i<land.length; i++) {
        for (let j=0; j<land[0].length; j++) {
            if (!check[i][j] && land[i][j]===1) {
                let oil = dfs(i, j, land, check, areaNum);
                area[areaNum] = oil;
                areaNum += 1;
            }
        }
    }
    for (let i=0; i<land[0].length; i++) {
        let areas = new Set([]);
        for (let j=0; j<land.length; j++) {
            if (land[j][i]!==0) {
                areas.add(land[j][i]);
            }
        }
        let temp = 0;
        for (a of areas) {
            if (area[a]) {
                temp += area[a];
            }
        }
        answer = Math.max(temp, answer);
    }
    return answer;
}