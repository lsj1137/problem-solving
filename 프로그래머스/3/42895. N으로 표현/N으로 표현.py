from collections import deque

def combine(dp1, dp2):
    result = set([])
    for n1 in dp1:
        for n2 in dp2:
            if n2==0:
                continue
            result.add(n1+n2)
            if n1-n2>-1:
                result.add(n1-n2)
            result.add(n1*n2)
            if n1//n2>-1:
                result.add(n1//n2)
    return list(result)

def solution(N, number):
    if N==number:
        return 1
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1,6):
        strN = str(N)*i
        if int(strN)<32001:
            dp[i].append(int(strN))
    for i in range(2, 9):
        for j in range(1,i):
            dp[i] += combine(dp[j], dp[i-j])
            dp[i] = list(set(dp[i]))
            if number in dp[i]:
                answer = i
                return answer
    return answer