import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        ArrayList<Integer> realBelt = new ArrayList<Integer>();
        ArrayList<Integer> tempBelt = new ArrayList<Integer>();
        
        for (int i=order.length+1; i>0; i--) {
            realBelt.add(i);
        }
        tempBelt.add(0);
        int index = 0;
        while (realBelt.size()>1 || tempBelt.size()>1) {
            int realTop = realBelt.get(realBelt.size()-1);
            int tempTop = tempBelt.get(tempBelt.size()-1);
            if (order[index] == realTop) {
                answer++;
                index++;
                realBelt.remove(realBelt.size()-1);
            } else if (order[index] == tempTop) {
                answer++;
                index++;
                tempBelt.remove(tempBelt.size()-1);
            } else if (order[index] > realTop) {
                tempBelt.add(realTop);
                realBelt.remove(realBelt.size()-1);
            } else {
                break;
            }
        }
        return answer;
    }
}