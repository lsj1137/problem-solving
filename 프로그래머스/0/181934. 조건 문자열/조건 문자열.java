class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        if (eq.equals("=") && n==m) {
            answer = 1;
        } else if (ineq.equals("<")) {
            if (n<m) {
                answer = 1;
            } else {
                answer = 0;
            }
        } else if (ineq.equals(">")) {
            if (n>m) {
                answer = 1;
            } else {
                answer = 0;
            }
        }
        return answer;
    }
}