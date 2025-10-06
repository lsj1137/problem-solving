def solution(money):
    answer = 0
    N = len(money)
    if N<3:
        answer = max(money)
    else:
        dp1 = money[:-1]
        dp2 = money[1:]
        for i in range(1, N-1):
            if i==1:
                dp1[i] = max(dp1[i], dp1[i-1])
                dp2[i] = max(dp2[i], dp2[i-1])
            else:
                dp1[i] = max(dp1[i-1], dp1[i]+dp1[i-2])
                dp2[i] = max(dp2[i-1], dp2[i]+dp2[i-2])
        maxDp1 = max(dp1[-1], dp1[-2])
        maxDp2 = max(dp2[-1], dp2[-2])
        answer = max(answer, maxDp1, maxDp2)
        # print(dp1)
        # print(dp2)
    return answer