function checkWin(board) {
    let winCase = new Set();
    if (board[0][0] === board[0][1] && board[0][1] === board[0][2]) {
        if (board[0][0]!=='.') winCase.add(board[0][0]);
    }
    if (board[1][0] === board[1][1] && board[1][1] === board[1][2]) {
        if (board[1][0]!=='.') winCase.add(board[1][0]);
    }
    if (board[2][0] === board[2][1] && board[2][1] === board[2][2]) {
        if (board[2][0]!=='.') winCase.add(board[2][0]);
    }
    if (board[0][0] === board[1][0] && board[1][0] === board[2][0]) {
        if (board[0][0]!=='.') winCase.add(board[0][0]);
    }
    if (board[0][1] === board[1][1] && board[1][1] === board[2][1]) {
        if (board[0][1]!=='.') winCase.add(board[0][1]);
    }
    if (board[0][2] === board[1][2] && board[1][2] === board[2][2]) {
        if (board[0][2]!=='.') winCase.add(board[0][2]);
    }
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
        if (board[0][0]!=='.') winCase.add(board[0][0]);
    }
    if (board[2][0] === board[1][1] && board[1][1] === board[0][2]) {
        if (board[2][0]!=='.') winCase.add(board[2][0]);
    }
    return winCase;
}

function solution(board) {
    let winCase = [...checkWin(board)];
    if (winCase.length>1) {
        return 0;
    }
    let oCount = 0;
    let xCount = 0;
    for (i of board) {
        for (j of i) {
            if (j==='O') {
                oCount += 1;
            } else if (j==='X') {
                xCount += 1;
            }
        }
    }
    if (oCount-xCount > 1 || oCount-xCount < 0) {
        return 0;
    }
    if (winCase[0] === 'X' && oCount-xCount!==0) {
        return 0;
    }
    if (winCase[0] === 'O' && oCount-xCount!==1) {
        return 0;
    }
    return 1;
}