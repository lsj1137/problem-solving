function solution(n)
{
    var answer = 0;
    for (c of n.toString()) {
        answer += parseInt(c);
    }
    return answer;
}