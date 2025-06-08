function makeCode (n) {
    let answer = [];
    for (let i=1; i<n-3; i++) {
        for (let j=i+1; j<n-2; j++) {
            for (let k=j+1; k<n-1; k++) {
                for (let l=k+1; l<n; l++) {
                    for (let m=l+1; m<n+1; m++) {
                        answer.push([i,j,k,l,m]);
                    }
                }
            }
        }
    }
    return answer;
}

function check(candidates, q, answer) {
    let newCandidates = [];
    for (let i=0; i<candidates.length; i++) {
        let same = 0;
        for (n of q){
            if (candidates[i].find((cn)=>cn===n)) {
                same += 1;
            }
        }
        if (same === answer) {
            newCandidates.push(candidates[i]);
        }
    }
    return newCandidates;
}

function solution(n, q, ans) {
    var answer = 0;
    let candidates = makeCode(n);
    for (let i=0; i<q.length; i++) {
        candidates = check(candidates, q[i], ans[i]);
    }
    answer = candidates.length;
    return answer;
}