import java.lang.Math;

class Solution {
    public int gcd(int a, int b) {
        int maxi = Math.max(a,b);
        int mini = Math.min(a,b);
        while (maxi % mini != 0) {
            int temp = mini;
            mini = maxi % mini;
            maxi = temp;
        }
        return mini;
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {};
        int numer3 = numer1 * denom2 + numer2 * denom1;
        int denom3 = denom1 * denom2;
        int gcdnd = gcd(numer3, denom3);
        answer = new int[]{numer3/gcdnd, denom3/gcdnd};
        return answer;
    }
}