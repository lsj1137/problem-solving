function solution(elements) {
    var answer = 0;
    let circle = [...elements, ...elements];
    let sums = new Set([]);
    for (let i=0; i<elements.length; i++) {
        let sumI = 0;
        for (let j=i; j<i+elements.length; j++) {
            sumI += circle[j];
            sums.add(sumI);
        }
    }
    answer = sums.size;
    return answer;
}