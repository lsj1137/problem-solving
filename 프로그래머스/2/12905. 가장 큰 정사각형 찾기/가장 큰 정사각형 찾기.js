function check(l, board) {
    let result = true;
    for (let x=1; x<board.length-l+1; x++) {
        for (let y=1; y<board[0].length-l+1; y++) {
            result = true;
            if (board[x+l-1][y+l-1] - board[x-1][y+l-1] - board[x+l-1][y-1] + board[x-1][y-1] !== l*l) {
                result = false;
            }
            if (result) {
                break;
            }
        }
        if (result) {
            break;
        }
    }
    return result
}

function solution(board)
{
    var answer = 0;
    let newBoard = Array.from(new Array(board.length+1), (_, i)=> Array.from(new Array(board[0].length+1), ()=> 0));
    for (let i=0; i<board.length+1; i++) {
        if (i===0) {
            continue
        }
        for (let j=0; j<board[0].length+1; j++) {
            if (j===0) {
                newBoard[i][j] = 0;
            } else {
                newBoard[i][j] = board[i-1][j-1] + newBoard[i][j-1];
            }
        }
        for (let j=0; j<board[0].length+1; j++) {
            newBoard[i][j] += newBoard[i-1][j];
        }
    }
    let L = Math.min(board.length, board[0].length);
    while (L>0) {
        if (check(L, newBoard)) {
            answer = L*L;
            break;
        }
        L -= 1;
    }
    return answer;
}