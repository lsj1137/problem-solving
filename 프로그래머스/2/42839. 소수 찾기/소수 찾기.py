import math

def solution(numbers):
    answer = 0
    result = []
    ln = len(numbers)
    ns = list(map(int,numbers))
    chk = [False]*ln
    st = [['',chk]]
    nst = []
    while st:
        n = st.pop()
        for i in range(ln):
            if not n[1][i]:
                n[1][i] = True
                num = int(str(n[0])+str(ns[i]))
                if pcheck(num) and num not in result:
                    result.append(num)
                nst.append([num,n[1][:]])
                n[1][i] = False
        if not st:
            st = nst
            nst = []
    answer = len(result)
    return answer

def pcheck(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True