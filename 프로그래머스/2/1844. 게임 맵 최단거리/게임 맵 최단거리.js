let dx = [-1, 0, 1, 0];
let dy = [0, 1, 0, -1];

function solution(maps) {
    var answer = 1;
    let [n,m] = [maps.length, maps[0].length];
    let [sp, ep] = [[0,0], [n-1,m-1]];
    let checked = Array.from({length:n}, ()=> Array.from({length:m}, ()=> false));
    checked[sp[0]][sp[1]] = true;
    let que = [sp];
    let nQue = [];
    let success = false;
    while (que.length>0) {
        let [x,y] = que.pop();
        if (x===ep[0] && y===ep[1]) {
            success = true;
            break;
        }
        for (let i=0; i<4; i++) {
            let nx = x+dx[i];
            let ny = y+dy[i];
            if (nx>-1 && ny>-1 && nx<n && ny<m && !checked[nx][ny] && maps[nx][ny]!==0) {
                checked[nx][ny] = true;
                nQue.push([nx,ny]);
            }
        }
        if (que.length===0) {
            answer += 1;
            que = nQue;
            nQue = [];
        }
    }
    if (!success) {
        answer = -1;
    }
    return answer;
}