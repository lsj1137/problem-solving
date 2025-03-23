function euclid (a, b) {
    let big = Math.max(a,b);
    let sml = Math.min(a,b);
    if (big % sml === 0) {
        return sml;
    } else {
        return euclid(sml, big % sml);
    }
} 

function solution(n, m) {
    var answer = [];
    let gcd = euclid(n, m);
    let lcm = n * m / gcd;
    answer = [gcd, lcm];
    return answer;
}