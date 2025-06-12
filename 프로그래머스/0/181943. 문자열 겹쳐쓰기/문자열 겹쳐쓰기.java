class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String bf_overwrite = my_string.substring(0,s);
        String af_overwrite = my_string.substring(s+overwrite_string.length());
        answer = bf_overwrite + overwrite_string + af_overwrite;
        return answer;
    }
}