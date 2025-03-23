function solution(price, money, count) {
    var answer = -1;
    let cost = count*(count+1)/2*price - money;
    answer = cost>0 ? cost : 0;
    return answer;
}