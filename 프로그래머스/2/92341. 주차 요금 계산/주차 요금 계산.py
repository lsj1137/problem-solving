import math

def solution(fees, records):
    answer = []
    dic = {}
    chk = {}
    for rec in records:
        ord = list(rec.split())
        time = list(map(int,ord[0].split(':')))
        time = time[0]*60 + time[1]
        if ord[1] not in dic and ord[2] == "IN":
            dic[ord[1]] = [time]
            chk[ord[1]] = False
        elif ord[2] == "IN":
            dic[ord[1]].append(time)
            chk[ord[1]] = False
        else:
            dic[ord[1]][-1] = time - dic[ord[1]][-1]
            chk[ord[1]] = True
    for k in dic:
        if not chk[k]:
            dic[k][-1] = 23*60+59 - dic[k][-1]
            chk[k] = True
        total = sum(dic[k])
        fee = fees[1]
        if total>fees[0]:
            fee += math.ceil((total-fees[0])/fees[2])*fees[3]
        dic[k] = fee
    answer = [dic[x] for x in sorted(dic.keys())]
    return answer