function solution(s) {
    var answer = '';
    let temp = [...s].sort((a,b)=>{
        if (a>b) {
            return -1;
        } else {
            return 1;
        }
    });
    answer = temp.join('');
    return answer;
}