class Solution {
    public String pushStr(String origin) {
        String result = origin.charAt(origin.length()-1) + origin.substring(0, origin.length()-1);
        return result;
    }
    public int solution(String A, String B) {
        int answer = -1;
        String curStr = A;
        for (int i=0; i<A.length(); i++) {
            if (curStr.equals(B)) {
                answer = i;
                break;
            }
            curStr = pushStr(curStr);
        }
        return answer;
    }
}