def check(x,y,m,park):
    for i in range(x,x+m):
        for j in range(y,y+m):
            if park[i][j] != "-1":
                return False
    return True

def solution(mats, park):
    answer = -1
    mats.sort(reverse = True)
    for m in mats:
        for i in range(len(park)-m+1):
            for j in range(len(park[0])-m+1):
                if check(i,j,m,park):
                    return m
    return answer