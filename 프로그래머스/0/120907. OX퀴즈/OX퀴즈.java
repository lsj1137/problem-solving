class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int index = 0;
        for (String exp: quiz) {
            String[] expArr = exp.split(" ");
            int a = Integer.parseInt(expArr[0]);
            int b = Integer.parseInt(expArr[2]);
            int r = Integer.parseInt(expArr[4]);
            String oper = expArr[1];
            if (oper.equals("+")) {
                answer[index++] = a+b==r ? "O" : "X";
            } else {
                answer[index++] = a-b==r ? "O" : "X";
            }
        }
        return answer;
    }
}