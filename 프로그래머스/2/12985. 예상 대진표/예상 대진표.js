function solution(n,a,b)
{
    var answer = 1;
    [a,b] = [a-1, b-1];
    while (Math.floor(a/2)!== Math.floor(b/2)) {
        a = Math.floor(a/2);
        b = Math.floor(b/2);
        answer += 1;
    }
    return answer;
}