def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        c = ''
        a = toBi(arr1[i],n)
        b = toBi(arr2[i],n)
        for j in range(n):
            if a[j]==b[j]=='0':
                c += ' '
            else:
                c += '#'
        answer.append(c)
    return answer

def toBi(n,l):
    r = ''
    while n>0:
        r += str(n%2)
        n//=2
    r = r[::-1].zfill(l)
    return r