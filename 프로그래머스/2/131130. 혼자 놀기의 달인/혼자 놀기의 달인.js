function dfs(i, cards, check, size) {
    check[i] = true;
    let next = cards[i]-1;
    if (!check[next]) {
        return dfs(next, cards, check, size+1);
    }
    return size;
}

function solution(cards) {
    var answer = 0;
    let check = Array.from(new Array(cards.length), ()=>false);
    let sizes = [];
    for (let i=0; i<cards.length; i++) {
        if (!check[i]) {
            sizes.push(dfs(i, cards, check, 1));
        }
    }
    sizes.sort((a,b)=>b-a);
    if (sizes.length>1) {
        answer = sizes[0] * sizes[1];
    }
    return answer;
}