function solution(nodes, edges) {
    var answer = [0,0];
    let tree = {};
    let checked = {};
    for (node of nodes){
        tree[node] = [];
        checked[node] = false;
    }
    for (edge of edges) {
        let [s,e] = edge;
        tree[s].push(e);
        tree[e].push(s);
    }
    for (node of nodes) {
        let que = [];
        let nodeTypes = [];
        if (!checked[node]) {
            que.push(node);
        } else {
            continue;
        }
        while (que.length>0) {
            let curNode = que.shift();
            checked[curNode] = true;
            if ((curNode%2===0 && tree[curNode].length%2===0) 
                || (curNode%2===1 && tree[curNode].length%2===1)) {
                nodeTypes.push(0);
            } else {
                nodeTypes.push(1);
            }
            for (nextNode of tree[curNode]) {
                if (!checked[nextNode]) {
                    que.push(nextNode);
                }
            }
        }
        let treeSum = nodeTypes.reduce((cur, acum)=>cur+acum,0);
        if (treeSum===nodeTypes.length-1) {
            answer[0] += 1;
        }
        if (treeSum===1) {
            answer[1] += 1;
        }
    }
    return answer;
}