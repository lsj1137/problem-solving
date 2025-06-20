import java.lang.*;

class Solution {
    public int calGcd (int a, int b) {
        int maxi = Math.max(a,b);
        int mini = Math.min(a,b);
        while (maxi%mini!=0) {
            int temp = maxi;
            maxi = mini;
            mini = temp % mini;
        }
        return mini;
    }
    
    public int calLcm (int a, int b, int gcd) {
        return a * b / gcd;
    }
    
    public int solution(int[] arr) {
        int answer = 1;
        for (int i=0; i<arr.length-1; i++) {
            int gcd = calGcd(arr[i], arr[i+1]);
            arr[i+1] = calLcm(arr[i], arr[i+1], gcd);
        }
        answer = arr[arr.length-1];
        return answer;
    }
}