class Solution {
    public int solution(int n) {
        int answer = 0;
        float start = n;
        int nums = 2;
        while (start>0) {
            if (start == (int)start) {
                answer += 1;
            }
            start = (float)n/nums - (float)(nums-1)/2;
            nums += 1;
        }
        return answer;
    }
}