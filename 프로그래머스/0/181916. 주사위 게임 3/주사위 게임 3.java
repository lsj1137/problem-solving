import java.lang.Math;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        if (a==b && b==c && c==d) {
            answer = 1111 * a;
        } else if ((a==b && b==c) || (a==b && b==d) || (a==c && c==d) || (b==c && c==d)) {
            if (a==b && b==c) {
                answer = (int) Math.pow(10*a+d, 2);
            } else if (a==b && b==d) {
                answer = (int) Math.pow(10*a+c, 2);
            } else if (a==c && c==d) {
                answer = (int) Math.pow(10*a+b, 2);
            } else {
                answer = (int) Math.pow(10*b+a, 2);
            }
        } else if ((a==b && c==d) || (a==c && b==d) || (a==d && b==c)) {
            if (a==b && c==d) {
                answer = (a+c) * Math.abs(a-c);
            } else {
                answer = (a+b) * Math.abs(a-b);
            }
        } else if (a==b || a==c || a==d || b==c || b==d || c==d) {
            if (a==b) {
                answer = c*d;
            } else if (a==c) {
                answer = b*d;
            } else if (a==d) {
                answer = c*b;
            } else if (c==b) {
                answer = a*d;
            } else if (d==b) {
                answer = a*c;
            } else {
                answer = a*b;
            }
        } else {
            answer = Math.min(a,b);
            answer = Math.min(answer,c);
            answer = Math.min(answer,d);
        }
        return answer;
    }
}