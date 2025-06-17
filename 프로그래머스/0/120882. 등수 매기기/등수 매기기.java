import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        Double[] avgs = new Double[score.length];
        for (int i=0; i<score.length; i++) {
            avgs[i] = (double)(score[i][0] + score[i][1])/(double)2;
        }
        Arrays.sort(avgs, (a,b)->Double.compare(b,a));
        int index = 0;
        for (int[] person: score) {
            int rank = 0;
            for (int i=0; i<avgs.length; i++) {
                if ((double)(person[0] + person[1]) / (double)2 == avgs[i]) {
                    rank = i+1;
                    break;
                }
            }
            answer[index++] = rank;
        }
        return answer;
    }
}