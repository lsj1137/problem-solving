N = int(input())
nl = list(map(int, input().split()))
nl.sort()
mixed = float("inf")

s, e = 0, len(nl)-1
answerS, answerE = s, e
while s<e:
    sumSE = nl[s]+nl[e]
    if abs(sumSE)<mixed:
        mixed = abs(sumSE)
        answerS, answerE = nl[s], nl[e]
    if sumSE>0:
        e -= 1
    else:
        s += 1
print(answerS, answerE)