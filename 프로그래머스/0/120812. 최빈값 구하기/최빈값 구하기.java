class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] count = new int[1000];
        for (int n: array) {
            count[n] += 1;
        }
        int max = -1;
        for (int i=0; i<count.length; i++) {
            if (count[i]>max){
                answer = i;
                max = count[i];
            } else if (count[i]==max) {
                answer = -1;
            }
        }
        return answer;
    }
}