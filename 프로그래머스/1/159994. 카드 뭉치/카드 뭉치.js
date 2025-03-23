function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    let [ind1, ind2] = [0,0];
    for (word of goal) {
        if (word === cards1[ind1]) {
            ind1+=1;
        } else if (word === cards2[ind2]) {
            ind2+=1;
        } else {
            answer = "No";
            break;
        }
    }
    return answer;
}