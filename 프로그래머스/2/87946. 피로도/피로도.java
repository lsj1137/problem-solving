import java.util.*;
import java.lang.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        int answer = 0;
        Arrays.sort(dungeons, (a,b)->{
            if (b[0]-b[1] != a[0]-a[1]) {
                return Integer.compare(b[0]-b[1], a[0]-a[1]);
            } else {
                return Integer.compare(a[1], b[1]);
            }
        });
        ArrayList<int[]> que = new ArrayList<int[]>();
        ArrayList<int[]> newQue = new ArrayList<int[]>();
        que.add(new int[]{k, 0, 0});
        while (que.size()>0) {
            int[] curValue = que.remove(0);
            int life = curValue[0];
            int index = curValue[1];
            int count = curValue[2];
            if (index<dungeons.length) {
                if (life >= dungeons[index][0]) {
                    newQue.add(new int[]{life - dungeons[index][1], index+1, count+1});
                }
                newQue.add(new int[]{life, index+1, count});
            } else {
                answer = Math.max(answer, count);
            }
            if (que.size()==0) {
                que = (ArrayList<int[]>) newQue.clone();
                newQue = new ArrayList<int[]>();
                continue;
            }
        }
        return answer;
    }
}