class Solution {
    public float calInc(int[] sp1, int[] sp2) {
        float result = (float)(sp1[1]-sp2[1]) / (float)(sp1[0]-sp2[0]);
        return result;
    }
    public int solution(int[][] dots) {
        if (calInc(dots[0], dots[1]) == calInc(dots[2], dots[3])) {
            return 1;
        } else if (calInc(dots[0], dots[2]) == calInc(dots[1], dots[3])) {
            return 1;
        } else if (calInc(dots[0], dots[3]) == calInc(dots[1], dots[2])) {
            return 1;
        }
        return 0;
    }
}