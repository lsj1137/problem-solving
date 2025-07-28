

function solution(m, n, board) {
    var answer = 0;
    let deletePoint = [];
    let newBoard = [];
    board.map((line)=>newBoard.push([...line]));
    let keepGoing = true;
    while (keepGoing) {
        for (let i=0; i<m-1; i++) {
            for (let j=0; j<n-1; j++) {
                if (newBoard[i][j] !== '0' && newBoard[i][j] === newBoard[i][j+1] && newBoard[i][j] === newBoard[i+1][j] && newBoard[i][j] === newBoard[i+1][j+1]) {
                    deletePoint.push([i,j]);
                    deletePoint.push([i+1,j]);
                    deletePoint.push([i,j+1]);
                    deletePoint.push([i+1,j+1]);
                }
            }
        }
        keepGoing = false;
        for (p of deletePoint) {
            let [x,y] = p;
            if (newBoard[x][y]!=='0') {
                keepGoing = true;
                answer += 1;
                newBoard[x][y] = '0';
            }
        }
        deletePoint = [];
        for (let j=0; j<n; j++) {
            for (let i=m-2; i>-1; i--) {
                if (newBoard[i][j]!=='0' && newBoard[i+1][j]==='0') {
                    let bottom = i+1;
                    while (bottom<newBoard.length-1 && newBoard[bottom+1][j] === '0') {
                        bottom+=1;
                    }
                    newBoard[bottom][j] = newBoard[i][j];
                    newBoard[i][j] = '0';
                }
            }
        }
    }
    
    return answer;
}