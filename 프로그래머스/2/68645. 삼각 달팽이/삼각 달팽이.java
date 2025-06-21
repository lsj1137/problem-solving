import java.util.*;

class Solution {
    public int[] solution(int n) {
        int x=0, y=0, cd=0, cn=1, nx=0, ny=0, end=n*(n+1)/2;
        int[] answer = new int[end];
        int[] dx = {1, 0, -1};
        int[] dy = {0, 1, -1};
        ArrayList<int[]> tri = new ArrayList<int[]>();
        for (int i=0;i<n;i++) {
            tri.add(new int[i+1]);
        }
        while (cn<=end) {
            tri.get(x)[y] = cn++;
            nx = x + dx[cd];
            ny = y + dy[cd];
            if (nx<0 || nx>tri.size()-1 || ny<0 || ny>tri.get(nx).length-1 || tri.get(nx)[ny]!=0) {
                cd = (cd+1) % 3;
                nx = x + dx[cd];
                ny = y + dy[cd];
            }
            x = nx;
            y = ny;
        }
        int index = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<tri.get(i).length; j++) {
                answer[index++] = tri.get(i)[j];
            }
        }
        return answer;
    }
}