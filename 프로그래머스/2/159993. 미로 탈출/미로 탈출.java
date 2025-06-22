import java.util.*;

class Solution {
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int bfs(ArrayList<int[]> que, String[] maps, boolean[][] checked, int[] goal) {
        ArrayList<int[]> newQue = new ArrayList<int[]>();
        int result = 0;
        boolean success = false;
        while (que.size()>0) {
            int[] p = que.remove(que.size()-1);
            int cx = p[0];
            int cy = p[1];
            if (cx == goal[0] && cy == goal[1]) {
                success = true;
                break;
            }
            for (int i=0; i<4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx>-1 && nx<maps.length && ny>-1 && ny<maps[0].length() && !checked[nx][ny]) {
                    checked[nx][ny] = true;
                    newQue.add(new int[]{nx, ny});
                }
            }
            if (que.size()==0) {
                que = (ArrayList<int[]>) newQue.clone();
                newQue = new ArrayList<int[]>();
                result += 1;
                continue;
            }
        }
        if (success) return result;
        else return -1;
    }
    
    public int solution(String[] maps) {
        int answer = 0;
        boolean[][] checked = new boolean[maps.length][maps[0].length()];
        boolean[][] checked2 = new boolean[maps.length][maps[0].length()];
        int[] start = new int[2], end = new int[2], lever = new int[2];
        for (int i=0; i<maps.length; i++) {
            for (int j=0; j<maps[i].length(); j++) {
                char c = maps[i].charAt(j);
                if (c == 'X') {
                    checked[i][j] = true;
                    checked2[i][j] = true;
                } else if (c == 'S') {
                    start[0] = i;
                    start[1] = j;
                    checked[i][j] = true;
                } else if (c == 'L') {
                    lever[0] = i;
                    lever[1] = j;
                    checked2[i][j] = true;
                } else if (c == 'E') {
                    end[0] = i;
                    end[1] = j;
                }
            }
        }
        ArrayList<int[]> que = new ArrayList<int[]>();
        que.add(start);
        answer += bfs(que, maps, checked, lever);
        if (answer != -1) {
            que = new ArrayList<int[]>();
            que.add(lever);
            int secondSearch = bfs(que, maps, checked2, end);
            if (secondSearch==-1) {
                answer = -1;
            } else {
                answer += secondSearch;
            }
        }
        return answer;
    }
}