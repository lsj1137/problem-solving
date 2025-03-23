function solution(n) {
    var answer = 0;
    let arr = [...(n.toString())];
    arr.sort((a,b)=>{
        if (a>b){
            return -1;
        } else {
            return 1;
        }
    })
    answer = parseInt(arr.join(''));
    return answer;
}