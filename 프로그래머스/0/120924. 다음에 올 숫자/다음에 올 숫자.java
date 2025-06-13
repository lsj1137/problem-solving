class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int[] rule = new int[2];
        rule[0] = common[1]-common[0];
        if (common[0]!=0) {
            rule[1] = common[1]/common[0];
        }
        if (common[2] == common[1] + rule[0]) {
            answer = common[common.length-1] + rule[0];
        } else {
            answer = common[common.length-1] * rule[1];
        }
        return answer;
    }
}