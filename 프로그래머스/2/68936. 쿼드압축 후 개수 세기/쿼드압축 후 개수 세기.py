def divide(arr, s1, e1, s2, e2):
    area = []
    line = []
    for i in range(s1, e1):
        for j in range(s2, e2):
            line.append(arr[i][j])
        area.append(line)
        line = []
    return area

def checkSame(arr):
    result = ''
    w = len(arr)
    if w==1:
        result = str(arr[0][0])
    else:
        area1 = divide(arr, 0, int(w/2), 0, int(w/2))
        result1 = checkSame(area1)
        
        area2 = divide(arr, 0, int(w/2), int(w/2), w)
        result2 = checkSame(area2)
        
        area3 = divide(arr, int(w/2), w, 0, int(w/2))
        result3 = checkSame(area3)
        
        area4 = divide(arr, int(w/2), w, int(w/2), w)
        result4 = checkSame(area4)
        if len(result1)==1 and result1==result2 and result2==result3 and result3==result4:
            result = result1
        else:
            result = result1 + result2 + result3 + result4
    return result
        
        
def solution(arr):
    answer = []
    resultStr = checkSame(arr)
    oneCount = sum(map(int,list(resultStr)))
    zeroCount = len(resultStr) - oneCount
    answer = [zeroCount, oneCount]
    return answer