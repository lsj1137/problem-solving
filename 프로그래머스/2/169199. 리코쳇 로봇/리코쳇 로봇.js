function solution(board) {
    var answer = 1;
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    let check = Array.from(new Array(board.length), ()=> Array.from(new Array(board[0].length),()=>false));
    let startX = 0;
    let startY = 0;
    for (let i=0; i<board.length; i++) {
        for (let j=0; j<board[0].length; j++) {
            if (board[i][j]==='R') {
                startX = i;
                startY = j;
            }
        }
    }
    let que = [[startX, startY]];
    check[startX][startY] = true;
    let nextQue = [];
    let findingRoute = true;
    while (findingRoute) {
        if (que.length === 0) {
            if (nextQue.length === 0) {
                answer = -1;
                break;
            }
            que = [...nextQue];
            nextQue = [];
            answer += 1;
        }
        let point = que.pop();
        for (let i=0; i<4; i++) {
            let np = [...point];
            let nx = dx[i];
            let ny = dy[i];
            while (np[0] + nx >= 0
                   && np[0] + nx <= board.length-1
                   && np[1] + ny >= 0
                   && np[1] + ny <= board[0].length-1
                   && board[np[0] + nx][np[1] + ny] !== 'D') {
                np[0] += nx;
                np[1] += ny;
            }
            if (!check[np[0]][np[1]]) {
                check[np[0]][np[1]] = true;
                if (board[np[0]][np[1]] === 'G') {
                    findingRoute = false;
                    break;
                }
                nextQue.push([np[0], np[1]]);
            }
        }
    }
    return answer;
}