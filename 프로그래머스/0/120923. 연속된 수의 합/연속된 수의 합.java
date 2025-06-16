import java.lang.Math;

class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        float avg = (float)total / num;
        int s = (int)(Math.ceil(avg) - num/2);
        int e = (int)(Math.floor(avg) + num/2);
        int index = 0;
        for (int i=s; i<e+1; i++) {
            answer[index++] = i;
        }
        return answer;
    }
}