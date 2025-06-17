import java.util.*;
import java.lang.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] answer = new int[numlist.length];
        Integer[] boxed = Arrays.stream(numlist)
                        .boxed()
                        .toArray(Integer[]::new);
        Arrays.sort(boxed, (a, b)-> {
            int temp = Integer.compare(Math.abs(a-n), Math.abs(b-n));
            if (temp!=0) {
                return temp;
            } else {
                return b-a;
            }
        });
        for (int i = 0; i < boxed.length; i++) {
            answer[i] = boxed[i];
        }
        return answer;
    }
}