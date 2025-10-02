import heapq

def solution(jobs):
    answer = 0
    jobs = [[j[0],j[1],i] for i,j in enumerate(jobs)]
    jobs.sort(key = lambda x:-x[0])
    que = []
    time = 0
    finishTime = 0
    returnTime = []
    
    while len(jobs)>0 or len(que)>0:
        # print(time)
        # print(jobs)
        # print(que)
        while len(jobs)>0 and time>=jobs[-1][0]:
            newJob = jobs.pop()
            heapq.heappush(que, [newJob[1], newJob[0], newJob[2]])
        if time>=finishTime and len(que)>0:
            nextJob = heapq.heappop(que)
            finishTime = time + nextJob[0]
            returnTime.append(finishTime - nextJob[1])
        time += 1
    answer = sum(returnTime)//len(returnTime)
    return answer