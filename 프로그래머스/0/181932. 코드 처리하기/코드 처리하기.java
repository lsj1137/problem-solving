class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        for (int i=0; i<code.length(); i++) {
            if (code.charAt(i) == '1') {
                if (mode == 0) {
                    mode = 1;
                } else {
                    mode = 0;
                }
            } else if ((mode == 0 && i%2==0) || (mode == 1 && i%2==1)) {
                answer += code.charAt(i);
            }
        }
        if (answer.length()==0) {
            answer = "EMPTY";
        }
        return answer;
    }
}