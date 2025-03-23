function solution(arr) {
    var answer = arr.reduce((s,v)=> s+=v,0)/arr.length;
    return answer;
}