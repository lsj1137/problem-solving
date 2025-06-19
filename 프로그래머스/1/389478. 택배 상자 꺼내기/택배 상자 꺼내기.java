import java.lang.*;
import java.util.*;

class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int[][] boxes = new int[(int)(Math.ceil((double)n/(double)w))][w];
        for (int[] boxLine: boxes) {
            Arrays.fill(boxLine, -1);
        }
        int boxNum = 1;
        int x=0, y=0;
        for (int i=0; i<boxes.length; i++) {
            int st = i%2==0 ? 0:w-1;
            int end = i%2==0 ? w:-1;
            int step = i%2==0 ? 1:-1;
            for (int j=st; i%2==0 ? j<end: j>end; j= j+step) {
                if (boxNum==num) {
                    x = i;
                    y = j;
                }
                boxes[i][j] = boxNum++;
                if (boxNum==n+1) break;
            }
            if (boxNum==n+1) break;
        }
        for (int i=x; i<boxes.length; i++) {
            if (boxes[i][y]!=-1) {
                answer += 1;
            }
        }
        return answer;
    }
}