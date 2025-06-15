import java.util.ArrayList;

class Solution {
    public boolean check(String s) {
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i)!='5' && s.charAt(i)!='0') return false;
        }
        return true;
    }
    
    public int[] solution(int l, int r) {
        int[] answer = {};
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int i=l; i<r+1; i++) {
            if (i%5==0 && check(Integer.toString(i))) {
                nums.add(i);
            }
        }
        if (nums.size()==0) {
            answer = new int[]{-1};
        } else {
            answer = new int[nums.size()];
            int index = 0;
            for (int num: nums) {
                answer[index++] = num;
            }
        }
        return answer;
    }
}