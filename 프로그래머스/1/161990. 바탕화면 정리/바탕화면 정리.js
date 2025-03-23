function solution(wallpaper) {
    var answer = [];
    let [minX, minY, maxX, maxY] = [51, 51, 0, 0];
    for (let x = 0; x<wallpaper.length; x++) {
        for (let y = 0; y<wallpaper[x].length; y++) {
            if (wallpaper[x][y]==='#') {
                minX = Math.min(minX, x);
                minY = Math.min(minY, y);
                maxX = Math.max(maxX, x);
                maxY = Math.max(maxY, y);
            }
        }
    }
    answer = [minX, minY, maxX+1, maxY+1];
    return answer;
}