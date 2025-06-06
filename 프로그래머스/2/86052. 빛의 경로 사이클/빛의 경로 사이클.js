function search(x, y, grid, check, dir) {
    let que = [[x,y,dir]];
    let result = 1;
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    
    while (que.length>0) {
        let [cx, cy, cd] = que.pop();
        check[cx][cy][cd] = true;
        let nd = cd;
        
        if (grid[cx][cy] === 'L') {
            nd -= 1;
            if (nd<0) {
                nd += 4;
            }
        } else if (grid[cx][cy] === 'R') {
            nd = (nd+1) % 4;
        }
        let nx = (cx + dx[nd])%grid.length ;
        if (nx<0) {
            nx += grid.length;
        }
        let ny = (cy + dy[nd])%grid[0].length;
        if (ny<0) {
            ny += grid[0].length;
        }
        if (!check[nx][ny][nd]) {
            que.push([nx, ny, nd]);
            result += 1;
        }
        
    }
    return result;
}

function solution(grid) {
    var answer = [];
    let check = Array.from(new Array(grid.length), ()=> Array.from(new Array(grid[0].length), ()=>[false, false, false, false]));
    for (let i=0; i<grid.length; i++) {
        for (let j=0; j<grid[0].length; j++) {
            for (let k=0; k<4; k++) {
                if (!check[i][j][k]) {
                    answer.push(search(i, j, grid, check, k));
                }
            }
        }
    }
    answer.sort((a,b)=>a-b);
    return answer;
}