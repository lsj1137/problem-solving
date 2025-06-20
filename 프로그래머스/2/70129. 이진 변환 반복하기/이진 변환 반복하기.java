class Solution {
    public String toBinary(int n) {
        String result = "";
        while (n>0) {
            result += n%2;
            n = n/2;
        }
        return result;
    }
    public int[] solution(String s) {
        int[] answer = new int[2];
        while (!s.equals("1")) {
            answer[0] += 1;
            int nextN = 0;
            for (int i=0; i<s.length(); i++) {
                if (s.charAt(i) == '0') {
                    answer[1] += 1;
                } else {
                    nextN += 1;
                }
            }
            s = toBinary(nextN);
            nextN = 0;
        }
        return answer;
    }
}