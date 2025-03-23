function solution(players, callings) {
    let rank = {};
    let rankName = {};
    let answer = [];
    for (let i=0; i<players.length; i++) {
        rank[i] = players[i];
        rankName[players[i]] = i;
    }
    for (name of callings) {
        let curRank = rankName[name];
        let curFaster = rank[curRank-1];
        rank[curRank] = curFaster;
        rank[curRank-1] = name;
        rankName[curFaster] = curRank;
        rankName[name] = curRank-1;
    }
    answer = Object.values(rank);
    return answer;
}