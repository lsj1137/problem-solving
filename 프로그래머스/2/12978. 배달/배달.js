function solution(N, road, K) {
    var answer = 1;
    let cost = Array.from({length:N}, ()=> new Object());
    for (r of road) {
        let [a,b,c] = r;
        a -= 1;
        b -= 1;
        cost[a]['dist'] = Infinity;
        cost[b]['dist'] = Infinity;
        if (cost[a][b] !== undefined){
            cost[a][b] = Math.min(cost[a][b], c);
        } else {
            cost[a][b] = c;
        }
        if (cost[b][a] !== undefined) {
            cost[b][a] = Math.min(cost[b][a], c);
        } else {
            cost[b][a] = c;
        }
    }
    let checked = Array.from({length:N}, ()=>false);
    cost[0].dist = 0;
    checked[0] = true;
    let que = [0];
    while (que.length>0) {
        let i = que.shift();
        let curNode = cost[i];
        for (n in curNode) {
            if (n!=='dist') {
                if (curNode.dist+curNode[n] < cost[n].dist) {
                    cost[n].dist = curNode.dist+curNode[n];
                    if (cost[n].dist <= K && !checked[n]) {
                        checked[n] = true;
                        answer += 1;
                    }
                    que.push(n);
                }
            }
        }
    }
    return answer;
}