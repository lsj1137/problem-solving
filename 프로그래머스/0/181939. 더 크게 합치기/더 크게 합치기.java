import java.lang.Math;

class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ab = Integer.toString(a) + Integer.toString(b);
        String ba = Integer.toString(b) + Integer.toString(a);
        answer = Math.max(Integer.valueOf(ab), Integer.valueOf(ba));
        return answer;
    }
}