function findRoute(ps) {
    let route = [ps[0]];
    for (let i=0; i<ps.length-1; i++) {
        let p1 = ps[i];
        let p2 = ps[i+1];
        let d = [-1, 1];
        let xStep = p1[0] > p2[0] ? d[0] : d[1];
        let yStep = p1[1] > p2[1] ? d[0] : d[1];
        let cp = [...p1];
        while (cp[0]!==p2[0]) {
            cp[0] += xStep;
            route.push([cp[0], cp[1]]);
        }
        while (cp[1]!==p2[1]) {
            cp[1] += yStep;
            route.push([cp[0], cp[1]]);
        }
    }
    return route;
}

function solution(points, routes) {
    var answer = 0;
    let routeDetails = [];
    let longest = 0;
    for (route of routes) {
        let ps = route.map((pn)=>points[pn-1]);
        let routeDetail = findRoute(ps);
        longest = Math.max(routeDetail.length, longest);
        routeDetails.push(routeDetail);
    }
    for (let i=0; i<longest; i++) {
        let checked = Array.from(new Array(101), ()=> Array.from(new Array(101), ()=> 0));
        routeDetails.map((r)=> {
            if(r.length>i) {
                let [x,y] = r[i];
                checked[x][y] += 1;
                if (checked[x][y]===2) {
                    answer += 1;
                }
            }
        })
    }
    return answer;
}