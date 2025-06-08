function solution(people, limit) {
    var answer = 0;
    people.sort((a,b)=>a-b);
    while (people.length>0) {
        answer += 1;
        let boat = people.pop();
        if (boat + people[0]<=limit) {
            boat += people.shift();
        }
    }
    return answer;
}