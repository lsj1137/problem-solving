function solution(cacheSize, cities) {
    var answer = 0;
    let cache = [];
    for (city of cities) {
        let cityName = city.toUpperCase();
        if (cache.find((c)=>c===cityName)) { // 히트
            answer += 1;
            let tmp = cache.filter((c)=>c!==cityName);
            tmp.push(cityName);
            cache = tmp;
        } else { // 미스
            answer += 5;
            if (cacheSize===0) {
                continue;
            }
            if (cache.length<cacheSize) {
                cache.push(cityName);
            } else {
                cache.shift();
                cache.push(cityName);
            }
        }
    }
    return answer;
}