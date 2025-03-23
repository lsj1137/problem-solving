function converter(route) {
    let [dir, degree] = route.split(' ');
    degree = parseInt(degree);
    if (dir === 'N') {
        return [-1, 0, degree];
    } else if (dir === 'E'){
        return [0, 1, degree];
    } else if (dir === 'S'){
        return [1, 0, degree];
    } else {
        return [0, -1, degree];
    } 
}

function solution(park, routes) {
    var answer = [];
    let point = [0, 0];
    let height = park.length;
    let width = park[0].length;
    for (let street = 0; street < park.length; street++) {
        for (let avenue = 0; avenue < park[street].length; avenue++) {
            if (park[street][avenue] === 'S') {
                point = [street, avenue];
            }
        }
    }
    for (route of routes) {
        let move = converter(route);
        nextP = [...point];
        for (let i = 0; i < move[2]; i++) {
            nextP[0] += move[0];
            nextP[1] += move[1];
            if (nextP[0] >= height || nextP[0] <= -1 ||
               nextP[1] >= width || nextP[1] <= -1 ||
               park[nextP[0]][nextP[1]] === 'X'
           ) {
                nextP = [...point];
                break;
            }
        }
        point = nextP;
    }
    answer = point;
    return answer;
}