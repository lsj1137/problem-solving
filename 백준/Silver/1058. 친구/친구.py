N = int(input())
friendDict = {}
result = 0

for i in range(N):
    friendDict[i] = []
    isFriendList = list(input())
    for j, v in enumerate(isFriendList):
        if v=="Y":
            friendDict[i].append(j)

for k in friendDict:
    friendOfK = friendDict[k]
    friendSet = set(friendOfK)
    for friend in friendOfK:
        friendSet = friendSet.union(set(friendDict[friend]))
    friendSet.discard(k)
    result = max(result, len(friendSet))
print(result)