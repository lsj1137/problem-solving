class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr.clone();
        for (int[] q: queries) {
            int temp = answer[q[0]];
            answer[q[0]] = answer[q[1]];
            answer[q[1]] = temp;
        }
        return answer;
    }
}