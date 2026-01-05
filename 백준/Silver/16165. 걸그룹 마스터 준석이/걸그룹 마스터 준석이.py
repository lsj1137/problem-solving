N, M = map(int, input().split())
groupDict = {}
for _ in range(N):
    groupName = input()
    groupDict[groupName] = []
    memCount = int(input())
    for _ in range(memCount):
        memberName = input()
        groupDict[groupName].append(memberName)
        groupDict[memberName] = groupName
    groupDict[groupName].sort()

for _ in range(M):
    question = input()
    qType = input()
    if qType=="0":
        for m in groupDict[question]:
            print(m)
    else:
        print(groupDict[question])