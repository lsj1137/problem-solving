def combination(arr, r):
    if r==1:
        return list(map(lambda x:[x] , arr))
    result = []
    for i, el in enumerate(arr):
        nextArr = arr[i+1:]
        for comb in combination(nextArr, r-1):
            result.append([el]+comb)
    return result

n, m = map(int, input().split())
people = []
hospital = []

for i in range(n):
    line = list(input().split())
    for j in range(n):
        if line[j]=='1':
            people.append((i,j))
        elif line[j]=='2':
            hospital.append((i,j))

distance = [[0]*len(people) for _ in range(len(hospital))]
for i, h in enumerate(hospital):
    for j, p in enumerate(people):
        distance[i][j] = abs(h[0]-p[0]) + abs(h[1]-p[1])
hospitalCombination = combination(list(range(len(hospital))), m)

answer = float('inf')
for selectedHospitals in hospitalCombination:
    temp = 0
    for i in range(len(people)):
        distForI = float('inf')
        for h in selectedHospitals:
            if distForI > distance[h][i]:
                distForI = distance[h][i]
        temp += distForI
        if temp>answer:
            break
    answer = min(answer, temp)
print(answer)
