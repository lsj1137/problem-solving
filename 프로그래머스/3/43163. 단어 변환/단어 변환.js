function checkClose(a,b) {
    let result = 0;
    for (let i=0; i<a.length; i++) {
        if (a[i] !== b[i]) {
            result += 1;
        }
    }
    return result===1;
}

function solution(begin, target, words) {
    var answer = 1;
    let tree = {};
    let newWords = [begin, ...words];
    let check = {};
    newWords.map((w)=>{
        tree[w] = []; 
        check[w] = false;
    });
    for (let i=0; i<newWords.length-1; i++) {
        for (let j=i+1; j<newWords.length; j++) {
            if (checkClose(newWords[i], newWords[j])) {
                if (tree[newWords[i]]) {
                    tree[newWords[i]].push(newWords[j]);
                }
                if (tree[newWords[j]]) {
                    tree[newWords[j]].push(newWords[i]);
                }
            }
        }
    }
    let que = [begin];
    let newQue = [];
    while (que.length>0) {
        let curWord = que.pop();
        check[curWord] = true;
        for (w of tree[curWord]) {
            if (w === target) {
                return answer;
            }
            if (!check[w]) {
                newQue.push(w);
            }
        }
        if (que.length===0) {
            que = [...newQue];
            newQue = [];
            answer += 1;
        }
    }
    answer = 0;
    return answer;
}