function solution(name) {
    var answer = 0;
    let index = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    let check = name.split('').map((c)=> c==='A'?true:false);
    check[0] = true;
    let que = [[0, check]];
    let nextQue = [];
    while (que.length>0) {
        let [i, curCheck] = que.pop();
        let newCheck = [...curCheck];
        newCheck[i] = true;
        if (newCheck.find((c)=>!c)===undefined) {
            break;
        }
        nextQue.push([i+1>name.length-1 ? 0 : i+1, newCheck]);
        nextQue.push([i-1<0 ? name.length-1 : i-1, newCheck]);
        if (que.length===0) {
            que = [...nextQue];
            nextQue = [];
            answer += 1;
        }
    }
    let curArr = Array.from(new Array(name.length), ()=>'A');
    for (let i=0; i<name.length; i++) {
        answer += Math.min(index[name[i]], 26-index[name[i]]);
        curArr[i] = name[i];
    }
    return answer;
}