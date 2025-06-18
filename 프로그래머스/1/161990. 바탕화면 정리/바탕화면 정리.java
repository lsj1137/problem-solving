class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {};
        int lux = 51, luy = 51, rdx = 0, rdy = 0;
        for (int i=0; i<wallpaper.length; i++) {
            for (int j=0; j<wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j)=='#') {
                    if (i < lux) {
                        lux = i;
                    }
                    if (i > rdx) {
                        rdx = i;
                    }
                    if (j < luy) {
                        luy = j;
                    }
                    if (j > rdy) {
                        rdy = j;
                    }
                }
            }
        }
        answer = new int[] {lux, luy, rdx+1, rdy+1};
        return answer;
    }
}