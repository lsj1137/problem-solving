class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String odds = "";
        String evens = "";
        for (int i = 0; i<num_list.length; i++) {
            if (num_list[i]%2==0) {
                evens += Integer.toString(num_list[i]);
            } else {
                odds += Integer.toString(num_list[i]);
            }
        }
        answer = Integer.valueOf(odds) + Integer.valueOf(evens);
        return answer;
    }
}