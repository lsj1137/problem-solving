class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int minX = 257, minY = 257;
        int maxX = -257, maxY = -257;
        for (int[] dot:dots) {
            if (minX > dot[0]) {
                minX = dot[0];
            }
            if (maxX < dot[0]) {
                maxX = dot[0];
            }
            if (minY > dot[1]) {
                minY = dot[1];
            }
            if (maxY < dot[1]) {
                maxY = dot[1];
            }
        }
        answer = (maxX - minX) * (maxY - minY);
        return answer;
    }
}