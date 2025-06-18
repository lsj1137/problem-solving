import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        boolean isReserve[] = new boolean[32];
        boolean isLost[] = new boolean[32];
        for (int r: reserve) {
            isReserve[r] = true;
        }
        for (int l: lost) {
            isLost[l] = true;
            if (isReserve[l]) {
                isReserve[l] = false;
                isLost[l] = false;
            }
        }
        Arrays.sort(lost);
        for (int l: lost) {
            if (!isLost[l]) continue;
            if (isReserve[l-1]) {
                isReserve[l-1] = false;
                continue;
            } else if (isReserve[l+1]) {
                isReserve[l+1] = false;
                continue;
            }
            n -= 1;
        }
        answer = n;
        return answer;
    }
}