function solution(food) {
    var answer = '';
    let reverseAnswer = '';
    for (let i=1; i<food.length; i++) {
        let count = Math.floor(food[i]/2);
        for (let j=0; j<count; j++) {
            answer += i.toString()
        }
    }
    reverseAnswer = [...answer].reduce((result,v)=>v+result, '');
    answer += '0' + reverseAnswer
    return answer;
}