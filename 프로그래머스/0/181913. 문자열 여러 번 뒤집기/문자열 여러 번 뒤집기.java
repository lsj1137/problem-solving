class Solution {
    public String reverse(String s) {
        String answer = "";
        for (int i=s.length()-1; i>-1; i--) {
            answer += s.charAt(i);
        }
        return answer;
    }
    
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        for (int[] query: queries) {
            int s = query[0];
            int e = query[1];
            answer = answer.substring(0, s) + reverse(answer.substring(s,e+1)) + answer.substring(e+1);
        }
        return answer;
    }
}