def solution(triangle):
    answer = 0
    h = len(triangle)
    for i in range(h-1):
        newtri = [0]*(i+2)
        for j in range(i+1):
            newtri[j] = max(newtri[j],triangle[i+1][j]+triangle[i][j])
            newtri[j+1] = max(newtri[j+1],triangle[i+1][j+1]+triangle[i][j])
        triangle[i+1] = newtri
    answer = max(triangle[-1])
    return answer