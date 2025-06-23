class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        boolean[][][] check = new boolean[11][11][4];
        int cx=5, cy=5, d=0;
        for (int i=0; i<dirs.length(); i++) {
            if (dirs.charAt(i) == 'U') {
                d = 0;
            } else if (dirs.charAt(i) == 'D') {
                d = 2;
            } else if (dirs.charAt(i) == 'R') {
                d = 1;
            } else {
                d = 3;
            }
            int nx = cx + dx[d];
            int ny = cy + dy[d];
            if (nx>-1 && nx<11 && ny>-1 && ny<11) {
                if (!check[cx][cy][d]) {
                    check[cx][cy][d] = true;
                    check[nx][ny][(d+2)%4] = true;
                    answer += 1;
                }
                cx = nx;
                cy = ny;
            }
        }
        return answer;
    }
}