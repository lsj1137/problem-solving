def solution(s):
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    key = dic.keys()
    for k in key:
        if k in s:
            s = s.replace(k,dic[k])
    answer = int(s)
    return answer