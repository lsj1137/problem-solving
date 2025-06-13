import java.util.Arrays;

class Solution {
    int[][] dir = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}};
    
    public int solution(int[][] board) {
        int answer = 0;
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j] == 1) {
                    for (int k=0; k<8; k++) {
                        int nx = i + dir[k][0];
                        int ny = j + dir[k][1];
                        if (nx>-1 && nx<board.length && ny>-1 && ny<board[0].length && board[nx][ny]!=1) {
                            board[nx][ny] = -1;
                        }
                    }
                }
            }
        }
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j]==0){
                    answer += 1;
                }
            }
        }
        return answer;
    }
}