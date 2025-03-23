def solution(n, k, cmd):
    answer = ['O']*n
    ll = [[0,0,i] for i in range(n)]
    deleted = []
    for i in range(n):
        ll[i][0] = i-1
        ll[i][1] = i+1
        if i == n-1:
            ll[i][1] = 0
    for c in cmd:
        c = list(c.split())
        if c[0] == 'U':
            for _ in range(int(c[1])):
                k = ll[k][0]
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                k = ll[k][1]
        elif c[0] == 'C':
            deleted.append(ll[k])
            temp = ll[k][0]
            ll[temp][1] = ll[k][1]
            ll[ll[k][1]][0] = temp
            if ll[k][1] == 0:
                k = ll[k][0]
            else:
                k = ll[k][1]
            n -= 1
        else:
            z = deleted.pop()
            ll[z[0]][1] = z[2]
            ll[z[1]][0] = z[2]
            n += 1
    for d in deleted:
        answer[d[2]] = 'X'
    answer = ''.join(answer)
    return answer