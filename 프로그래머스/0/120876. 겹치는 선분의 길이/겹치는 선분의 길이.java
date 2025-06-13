import java.lang.Math;
import java.util.ArrayList;

class Solution {
    public void calOverlap(int[] line1, int[] line2, boolean[] check) {
        int start = Math.max(line1[0], line2[0]);
        int end = Math.min(line1[1], line2[1]);
        if (start<end) {
            for (int i=start; i<end+1; i++) {
                check[i+100] = true;
            }
        }
    }
    
    public int solution(int[][] lines) {
        int answer = 0;
        boolean[] check = new boolean[201];
        
        calOverlap(lines[0], lines[1], check);
        calOverlap(lines[1], lines[2], check);
        calOverlap(lines[0], lines[2], check);
        
        for (int i=0; i<200; i++) {
            if (check[i] && check[i+1]) {
                answer += 1;
            }
        }
        
        return answer;
    }
}