class Solution {
    public boolean containThree(int n) {
        if (n%3==0) return true;
        String sn = Integer.toString(n);
        for (int i=0; i<sn.length(); i++) {
            if (sn.charAt(i)=='3') {
                return true;
            }
        }
        return false;
    }
    
    public int solution(int n) {
        int answer = 0;
        for (int i=0; i<n; i++) {
            answer += 1;
            while (containThree(answer)) {
                answer += 1;
            }
        }
        return answer;
    }
}