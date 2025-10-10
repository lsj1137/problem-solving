def compareAndReplace(count, a, b, isDouble):
    if sum(count[a]) == float('inf') or sum(count[a]) > sum(count[b])+1:
        # print(a,count[a], b, count[b], '!')
        count[a] = count[b][:]
        if isDouble:
            count[a][1] += 1
        else:
            count[a][0] += 1
    if sum(count[a]) == sum(count[b])+1 and count[a][0]<=count[b][0]:
        if not isDouble:
            # print(a,count[a], b, count[b], '?')
            count[a] = count[b][:]
            count[a][0] += 1
    return
    

def solution(target):
    answer = []
    count = [[float('inf'), float('inf')] for i in range(100001)]
    for i in range(1,61):
        if i<=20:
            count[i][0] = 1
            count[i][1] = 0
        elif i==50:
            count[i][0] = 1
            count[i][1] = 0
        elif i%2==0 and i//2<=20:
            count[i][1] = 1
            count[i][0] = 0
        elif i%3==0 and i//3<=20:
            count[i][1] = 1
            count[i][0] = 0
    
    for i in range(1, target+1):
        for j in range(1,21):
            if i-j<1:
                continue
            compareAndReplace(count, i, i-j, False)
        for j in range(1,21):
            if i-j*2>0:
                compareAndReplace(count, i, i-j*2, True)
            if i-j*3>0:
                compareAndReplace(count, i, i-j*3, True)
        if i-50>0:
            compareAndReplace(count, i, i-50, False) 
        
        
    answer = [sum(count[target]), count[target][0]]
    return answer