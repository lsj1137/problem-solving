def nToDec(n, b):
    result = 0
    i = 0
    while b>0:
        result += (b%10) * (n**i)
        b //= 10
        i += 1
    return result

def decToN(n, d):
    result = ''
    while d>0:
        result += str(d%n)
        d //= n
    if result == '':
        result = '0'
    return int(result[::-1])

def parse(expArr):
    if expArr[1]=='+':
        return [int(expArr[0]), int(expArr[2])]
    else:
        return [int(expArr[0]), -int(expArr[2])]

def checkAbleNotations(ableNotation, n1, n2, n3):
    for i in range(2,10):
        if not ableNotation[i]:
            continue
        if n2>=0:
            if not (decToN(i, nToDec(i, n1) + nToDec(i, n2)) == n3):
                ableNotation[i] = False
        else:
            if not (decToN(i, nToDec(i, n1) - nToDec(i, -n2)) == n3):
                ableNotation[i] = False
    return

def checkAbleAnswers(ableNotation, n1, n2):
    result = set([])
    for i in range(2,10):
        if not ableNotation[i]:
            continue
        if n2>=0:
            sums = decToN(i, nToDec(i, n1) + nToDec(i, n2))
            result.add(sums)
        else:
            sums = decToN(i, nToDec(i, n1) - nToDec(i, -n2))
            result.add(sums)
    return list(result)
    
    
def solution(expressions):
    answer = []
    ableNotation = [True]*10
    expressions = sorted([list(exp.split()) for exp in expressions], key=lambda x:x[4])
    for expArr in expressions:
        n1, n2, n3 = expArr[0], expArr[2], expArr[4]
        if n3=='X':
            ns = set(list(n1+n2))
        else:
            ns = set(list(n1+n2+n3))
        mn = max(ns)
        for i in range(int(mn)+1):
            ableNotation[i] = False
            
    for expArr in expressions:
        n1, n2 = parse(expArr)
        if expArr[4]=='X':
            ableAnswers = checkAbleAnswers(ableNotation, n1, n2)
            if len(ableAnswers)==1:
                expArr[4] = str(ableAnswers[0])
                answer.append(expArr)
            else:
                expArr[4] = '?'
                answer.append(expArr)
        else:
            n3 = int(expArr[4])
            checkAbleNotations(ableNotation, n1, n2, n3)
    answer = [' '.join(a) for a in answer]
    return answer