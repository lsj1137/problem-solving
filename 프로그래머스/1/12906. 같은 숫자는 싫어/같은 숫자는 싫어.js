function solution(arr)
{
    var answer = [];
    let last = '';
    for (val of arr) {
        if (val !== last) {
            answer.push(val);
            last = val;
        }
    }
    return answer;
}