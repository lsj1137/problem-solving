import java.util.*;

class Solution {
    public boolean check(String s) {
        boolean result = true;
        ArrayList<Character> parentheses = new ArrayList<Character>();
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i)=='(' || s.charAt(i)=='[' || s.charAt(i)=='{') {
                parentheses.add(s.charAt(i));
            } else {
                if (parentheses.size() < 1) {
                    return false;
                }
                if (s.charAt(i)==')' && parentheses.get(parentheses.size()-1) == '(') {
                    parentheses.remove(parentheses.size()-1);
                } else if (s.charAt(i)==']' && parentheses.get(parentheses.size()-1) == '[') {
                    parentheses.remove(parentheses.size()-1);
                } else if (s.charAt(i)=='}' && parentheses.get(parentheses.size()-1) == '{') {
                    parentheses.remove(parentheses.size()-1);
                } else {
                    return false;
                }
            }
        }
        if (parentheses.size()>0) {
            result = false;
        }
        return result;
    }
    public int solution(String s) {
        int answer = 0;
        for (int i=0; i<s.length(); i++) {
            String s1 = s.substring(i);
            String s2 = s.substring(0,i);
            if (check(s1+s2)) {
                answer += 1;
            }
        }
        
        return answer;
    }
}