function getCombinations(arr, r) {
    const results = [];
    if (r === 1) return arr.map(value => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, r - 1); 
        const attached = combinations.map(combination => [fixed, ...combination]); 
        results.push(...attached);
    });

    return results;
}

function check(cols, relation) {
    let selected = new Set(relation.map((row)=> {
        let newRow = "";
        for (col of cols) {
            newRow+=row[col];
        }
        return newRow; 
    }));
    if (selected.size !== relation.length) {
        return false;
    } else {
        return true;
    }
}

function minCheck(combination, arr) {
    let answer = true;
    let sc1 = new Set(combination);
    for (combi of arr) {
        let sc2 = new Set(combi);
        if (isSubsetOf(sc2, sc1)){
            answer = false;
        }
    }
    return answer;
}

function isSubsetOf(a,b) {
    let answer = 0;
    for (n of a) {
        if (b.has(n)){
            answer += 1;
        }
    }
    if (answer===a.size) {
        return true;
    } else {
        return false;
    }
}

function solution(relation) {
    var answer = 0;
    let answerArr = [];
    const colNum = relation[0].length;
    let cols = Array.from(new Array(colNum), (_,i)=>i);
    let checked = Array.from(new Array(colNum), ()=>false);
    for (let i=1; i<colNum+1; i++) {
        let combinations = getCombinations(cols,i);
        for (combination of combinations) {
            if (!minCheck(combination, answerArr)) continue;
            if (check(combination, relation)){
                answerArr.push(combination);
                answer += 1;
            }
        }
    }
    return answer;
}