def combination(arr, r): # 조합 (확률과 통계)
    result = []
    if r==1:
        return [[n] for n in arr]
    for i, n in enumerate(arr):
        remain = arr[i+1:]
        combiRest = combination(remain, r-1)
        for combi in combiRest:
            result.append([n] + combi)
    return result

N = int(input())
hands = [list(map(int, input().split())) for _ in range(N)]
result = 0
maxi = 0

for i,deck in enumerate(hands):
    combi = combination(deck, 3)
    maxCombi = max(map(lambda n : sum(n)%10, combi))
    if maxi<=maxCombi:
        result = i+1
        maxi = maxCombi

print(result)