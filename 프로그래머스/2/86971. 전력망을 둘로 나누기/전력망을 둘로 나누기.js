function dfs(curNode, curWire, nodes, check, len) {
    check[curWire] = true;
    for (node of nodes[curNode]) {
        let minNode = Math.min(curNode, node);
        let maxNode = Math.max(curNode, node);
        if (!check[[minNode, maxNode]]) {
            len = dfs(node, [minNode, maxNode], nodes, check, len+1);
        }
    }
    return len;
}

function solution(n, wires) {
    var answer = n;
    let nodes = {};
    let check = {};
    for (let i=1; i<n+1; i++) {
        nodes[i] = []
    }
    for (wire of wires) {
        nodes[wire[0]].push(wire[1]);
        nodes[wire[1]].push(wire[0]);
        check[wire] = false;
    }
    for (wire of wires) {
        check[wire] = true;
        let a = dfs(wire[0], wire, nodes, {...check}, 1);
        let b = dfs(wire[1], wire, nodes, {...check}, 1);
        answer = Math.min(Math.abs(a-b), answer);
        check[wire] = false;
    }
    return answer;
}
