class Solution {
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int cx = 0;
        int cy = 0;
        int cd = 0;
        int num = 1;
        while (num<n*n) {
            answer[cx][cy] = num++;
            int nx = cx + dx[cd];
            int ny = cy + dy[cd];
            while (nx<0 || ny<0 || nx>n-1 || ny>n-1 || answer[nx][ny]!=0) {
                cd = (cd+1) % 4;
                nx = cx + dx[cd];
                ny = cy + dy[cd];
            }
            cx = nx;
            cy = ny;
        }
        answer[cx][cy] = num;
        return answer;
    }
}