function solution(n, w, num) {
    let answer = 0;
    const rowNum = Math.ceil(n/w);
    let boxes = new Array(rowNum);
    let targetRow = 0;
    let targetCol = 0;
    for (let i=0; i<rowNum; i++) {
        boxes[i] = Array.from(new Array(w), (_,j)=>{
            let boxNum;
            if (i%2==0) {
                boxNum = i*w+j+1;
            } else {
                boxNum = (i+1)*w-j;
            }
            if (boxNum === num) {
                targetRow = i;
                targetCol = j;
            }
            if (boxNum<=n) return boxNum;
            else return -1;
        });
    }
    if (boxes[rowNum-1][targetCol] === -1) answer -= 1;
    answer += rowNum-targetRow;
    return answer;
}