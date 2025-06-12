class Solution {
    public int sumOdds(int n) {
        int result = 0;
        while (n>0) {
            result += n;
            n = n-2;
        }
        return result;
    }
    
    public int sumEvens(int n) {
        int result = 0;
        while (n>0) {
            result += n*n;
            n = n-2;
        }
        return result;
    }
    
    public int solution(int n) {
        int answer = 0;
        if (n%2==0) {
            answer = sumEvens(n);
        } else {
            answer = sumOdds(n);
        }
        return answer;
    }
}