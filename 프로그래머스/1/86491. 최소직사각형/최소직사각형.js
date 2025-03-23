function solution(sizes) {
    var answer = 0;
    let [width, height] = [0, 0];
    for (size of sizes) {
        let sml = Math.min(size[0], size[1]);
        let big = Math.max(size[0], size[1]);
        width = Math.max(big, width);
        height = Math.max(sml, height);
    }
    answer = width * height
    return answer;
}