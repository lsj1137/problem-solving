import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        ArrayList<Integer> numArr = new ArrayList<Integer>();
        while (n!=1) {
            numArr.add(n);
            if (n%2==0) {
                n = n / 2;
            } else {
                n = 3*n + 1;
            }
        }
        numArr.add(1);
        answer = new int[numArr.size()];
        int index = 0;
        for (int num: numArr) {
            answer[index++] = num;
        }
        return answer;
    }
}