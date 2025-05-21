function solution(storey) {
    var answer = 0;
    let division = 10;
    let que = [[storey, 0]];
    let newQue = [];
    while (que.length>0) {
        // console.log(que);
        let n = que.shift();
        let units = n[0]%10;
        let newElement = newQue.find((e)=>e[0] === (n[0]-units)/10);
        if (newElement) {
            newElement[1] = Math.min(newElement[1], n[1]+units);
        } else {
            newQue.push([(n[0]-units)/10, n[1]+units]);  
        }
        let newElement2 = newQue.find((e)=>e[0] === (n[0]+(10-units))/10);
        if (newElement2) {
            newElement2[1] = Math.min(newElement2[1], n[1]+(10-units));
        } else {
            newQue.push([(n[0]+(10-units))/10, n[1]+(10-units)]);
        }
        if (que.length===0 && newQue[0][0] > 0) {
            // console.log("change!!");
            que = [...newQue];
            newQue = [];
        }
    }
    // console.log("change!!");
    // console.log(newQue);
    answer = Math.min(...newQue.map(e=>e[0]+e[1]));
    return answer;
}
