import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        int[] newArr = arr.clone();
        for (int i=0; i<query.length; i++) {
            if (i%2==0) {
                newArr = Arrays.copyOfRange(newArr, 0, query[i]+1);
            } else {
                newArr = Arrays.copyOfRange(newArr, query[i], newArr.length);
            }
        }
        answer = newArr.clone();
        return answer;
    }
}