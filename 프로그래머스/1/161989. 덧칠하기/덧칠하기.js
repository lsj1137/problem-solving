function solution(n, m, section) {
    var answer = 0;
    let wall = Array.from(new Array(100001), ()=>true);
    for (point of section) {
        wall[point] = false;
    }
    for (let i=1; i<wall.length; i++) {
        if (!wall[i]) {
            answer += 1;
            for (let j=i; j<i+m; j++) {
                wall[j] = true;
            }
        }
    }
    return answer;
}