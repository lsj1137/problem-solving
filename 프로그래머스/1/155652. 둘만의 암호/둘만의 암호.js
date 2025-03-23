function solution(s, skip, index) {
    var answer = '';
    let seq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    let seqObj = {};
    seq.filter((c)=> !skip.includes(c))
        .map((c,i)=> seqObj[c] = i);
    for (c of s) {
        let newInd = seqObj[c] + index;
        while (newInd >= Object.keys(seqObj).length) {
            newInd -= Object.keys(seqObj).length;
        }
        let newChar = Object.entries(seqObj).find((entry)=>entry[1] === newInd)[0];
        answer += newChar;
    }
    return answer;
}