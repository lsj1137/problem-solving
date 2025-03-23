function solution(bandage, health, attacks) {
    var answer = 0;
    let t = 0;
    let maxHealth = health;
    let combo = -1;
    let curAttack = 0;
    let curHealth = health;
    while (t <= attacks[attacks.length-1][0]) {
        if (t === attacks[curAttack][0]) {
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
        if (combo === bandage[0]) {
            curHealth = curHealth + bandage[2] > maxHealth ? maxHealth : curHealth + bandage[2];
            combo = 0;
        }
        t += 1;
    }
    answer = curHealth;
    return answer;
}