import java.util.*;
class Solution {
    public boolean check(String s) {
        ArrayList<Character> p = new ArrayList<Character>();
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i)=='(') {
                p.add('(');
            } else {
                if (p.size()<1) return false;
                if (p.get(p.size()-1) == '(') {
                    p.remove(p.size()-1);
                } else {
                    return false;
                }
            }
        }
        if (p.size()>0) return false;
        return true;
    }
    public String flip(String s) {
        String result = "";
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                result += ')';
            } else {
                result += '(';
            }
        }
        return result;
    }
    public String solution(String p) {
        String answer = "";
        int countL = 0;
        int countR = 0;
        String u="", v="";
        for (int i=0; i<p.length(); i++) {
            if (p.charAt(i) == '(') {
                countL += 1;
            } else {
                countR += 1;
            }
            if (countL!=0 && countL==countR) {
                u = p.substring(0,i+1);
                v = p.substring(i+1);
                if (check(u)) {
                    answer = u + solution(v);
                } else {
                    answer = "(" + solution(v) + ")" + flip(u.substring(1,u.length()-1));
                }
                break;
            }
        }
        return answer;
    }
}