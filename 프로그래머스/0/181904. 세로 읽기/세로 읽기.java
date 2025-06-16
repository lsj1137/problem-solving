class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        int cur = c-1;
        while (cur<my_string.length()) {
            answer += my_string.charAt(cur);
            cur += m;
        }
        return answer;
    }
}