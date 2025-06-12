class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int muls = 1;
        int sums = 0;
        for (int i = 0; i<num_list.length; i++) {
            muls *= num_list[i];
            sums += num_list[i];
        }
        if (muls < sums*sums) {
            answer = 1;
        }
        return answer;
    }
}