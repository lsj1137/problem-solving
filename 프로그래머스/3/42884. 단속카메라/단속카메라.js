function solution(routes) {
    var answer = 1;
    routes.sort((a,b)=>a[1]-b[1]);
    let std = routes[0][1];
    for (route of routes) {
        if (route[0]>std) {
            answer += 1;
            std = route[1];
        }
    }
    return answer;
}