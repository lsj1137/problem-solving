function findStart(candidates, nodes) {
    for (key of candidates) {
        let visited = {};
        visited[key] = 1;
        let nNode = nodes[key][0];
        let isStart = false;
        while (nNode!==undefined) {
            if (visited[nNode]!==undefined) {
                if (nNode == key) {
                    break;
                } else {
                    return key;
                }
            }
            visited[nNode] = 1;
            nNode = nodes[nNode][0];
        }
        if (nNode === undefined) {
            return key;
        }
    }
}

function checkType(start, nodes) {
    let visited = {};
    visited[start] = 1;
    if (nodes[start].length===2) {
        return [0,0,1];
    }
    let nNode = nodes[start][0];
    while (nNode!==undefined) {
        if (visited[nNode]!==undefined) {
            return [1,0,0];
        }
        visited[nNode] = 1;
        if (nodes[nNode].length===2) {
            return [0,0,1];
        }
        nNode = nodes[nNode][0];
    }
    return [0,1,0];
}

function solution(edges) {
    var answer = [];
    let nodes = {};
    for (edge of edges) {
        let [s,e] = edge;
        if (nodes[s]===undefined) {
            nodes[s] = [e];
        } else {
            nodes[s].push(e);
        }
        if (nodes[e]===undefined) {
            nodes[e] = [];
        }
    }
    let start = Object.keys(nodes).find((k)=>nodes[k].length>2);
    let candidates = Object.keys(nodes).filter((k)=>nodes[k].length>=2);
    if (start===undefined) {
        if (candidates.length===1) {
            start = candidates[0];
        } else {
            start = findStart(candidates, nodes);
        }
    }
    let startBranches = nodes[start];
    let [doughnut, stick, eight] = [0,0,0];
    for (branch of startBranches) {
        let graphType = checkType(branch, nodes);
        doughnut += graphType[0];
        stick += graphType[1];
        eight += graphType[2];
    }
    answer = [Number(start), doughnut, stick, eight];
    return answer;
}