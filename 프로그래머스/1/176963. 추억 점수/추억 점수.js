function solution(name, yearning, photo) {
    let answer = [];
    let point = {};
    for (n in name) {
        point[name[n]] = yearning[n];
    }
    for (pic of photo) {
        let sum = 0;
        for (person of pic) {
            if (point[person]) sum += point[person];
        }
        answer.push(sum);
    }
    return answer;
}