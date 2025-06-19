class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int t = 0;
        int maxHealth = health;
        int combo = -1;
        int curAttack = 0;
        int curHealth = health;
        while (t <= attacks[attacks.length-1][0]) {
            if (t == attacks[curAttack][0]) {
                curHealth -= attacks[curAttack][1];
                combo = 0;
                if (curHealth <= 0) {
                    return -1;
                }
                curAttack += 1;            
            } else {
                combo += 1;
                curHealth = curHealth + bandage[1] > maxHealth ? maxHealth : curHealth + bandage[1];
            }
            if (combo == bandage[0]) {
                curHealth = curHealth + bandage[2] > maxHealth ? maxHealth : curHealth + bandage[2];
                combo = 0;
            }
            t += 1;
        }
        answer = curHealth;
        return answer;
    }
}