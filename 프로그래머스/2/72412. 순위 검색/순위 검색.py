lang = {'cpp':'0', 'java':'1', 'python':'2', '-':'?'}
domain = {'backend':'0', 'frontend':'1', '-':'?'}
career = {'junior':'0', 'senior':'1', '-':'?'}
food = {'chicken':'0', 'pizza':'1', '-':'?'}

def infoToCode(a,b,c,d,e):
    result = ''
    result += lang[a]
    result += domain[b]
    result += career[c]
    result += food[d]
    return [result, int(e)]

def codeToCate(code):
    que = ['']
    for i in range(4):
        newQue = []
        while len(que)>0:
            c = que.pop()
            newQue.append(c+'?')
            newQue.append(c+code[i])
        que = newQue
    return que

def search(db, query):
    qCondition, qScore = query
    result = 0
    if qCondition not in db:
        return result
    sameConditions = db[qCondition]
    start = 0
    end = len(sameConditions)-1
    while start<=end:
        mid = (start+end)//2
        if sameConditions[mid]<qScore:
            start = mid+1
        else:
            end = mid-1
    result=len(sameConditions)-start
    return result

def solution(info, query):
    answer = []
    db = {}
    for i in info:
        data = infoToCode(*i.split())
        cate = codeToCate(data[0])
        for c in cate:
            if c in db:
                db[c].append(data[1])
            else:
                db[c] = [data[1]]
    for key in db.keys():
        db[key].sort()
    for q in query:
        ql = list(q.split(' and '))
        d,e = ql.pop().split()
        ql.append(d)
        ql.append(e)
        qData = infoToCode(*ql)
        answer.append(search(db, qData))
        
    return answer