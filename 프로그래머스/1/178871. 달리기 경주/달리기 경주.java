import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        HashMap<String, Integer> ranking = new HashMap<String, Integer>();
        for (int i=0; i<players.length; i++) {
            ranking.put(players[i], i);
        }
        for (String name: callings) {
            int curRank = ranking.get(name);
            String temp = players[curRank-1];
            ranking.put(name, ranking.get(name) - 1);
            ranking.put(temp, ranking.get(temp) + 1);
            players[curRank-1] = players[curRank];
            players[curRank] = temp;
        }
        answer = players.clone();
        return answer;
    }
}