class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        int cur = r;
        while (cur<code.length()){
            answer += code.charAt(cur);
            cur += q;
        }
        return answer;
    }
}