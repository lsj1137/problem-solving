// 점화식 f(n) = ((f(n - 2) x 4 % 1,000,000,007) - (f(n - 4) % 1,000,000,007) + 1,000,000,007) % 1,000,000,007
let arr = [0, 3, 11];
function solution(n) {
    var answer = 0;
    if (n%2===1) return 0;
    let halfN = n/2;
    if (halfN<arr.length) {
        return arr[halfN];
    }
    answer = (solution(n-2) * 4 % 1000000007 - solution(n-4) % 1000000007 + 1000000007) % 1000000007;
    arr.push(answer);
    return answer;
}