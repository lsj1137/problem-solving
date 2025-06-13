class Solution {
    public boolean checkTwo(String word) {
        if (word.length()<2) return false;
        String front = word.substring(0,2);
        if (front.equals("ye") || front.equals("ma")) {
            return true;
        }
        return false;
    }
    
    public boolean checkThree(String word) {
        if (word.length()<3) return false;
        String front = word.substring(0,3);
        if (front.equals("aya") || front.equals("woo")) {
            return true;
        }
        return false;
    }
    
    public int solution(String[] babbling) {
        int answer = 0;
        for (String word: babbling) {
            String curWord = word;
            while (true) {
                if (!checkTwo(curWord) && !checkThree(curWord)) {
                    break;
                }
                if (checkTwo(curWord)) {
                    curWord = curWord.substring(2);
                }
                if (checkThree(curWord)) {
                    curWord = curWord.substring(3);
                }
                if (curWord.length() == 0) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}