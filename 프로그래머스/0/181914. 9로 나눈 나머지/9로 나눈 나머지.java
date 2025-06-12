class Solution {
    public int solution(String number) {
        int answer = 0;
        int sumN = 0;
        for (int i=0; i<number.length(); i++) {
            sumN += number.charAt(i) - '0';
        }
        answer = sumN % 9;
        return answer;
    }
}