import math

def solution(r1, r2):
    r = 0
    for i in range(0,r2+1):
        y2 = math.floor(math.sqrt(r2**2 - i**2))
        if i<r1+1:
            y1 = math.ceil(math.sqrt(r1**2 - i**2))
        else:
            y1 = 0
        r += (y2-y1+1)
        
    r -= (r2-r1+1)
        
    answer = r * 4
    return answer