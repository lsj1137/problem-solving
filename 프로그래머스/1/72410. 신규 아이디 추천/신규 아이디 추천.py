def solution(new_id):
    sp = "~!@#$%^&*()=+[{]}:?,<>/"
    answer = ''
    nid = ''.join(c for c in new_id.lower() if c not in sp).strip('.')
    for i in range(len(nid)):
        if nid[i]=='.' and nid[i+1]=='.':
            continue
        answer+=nid[i]
    if not answer:
        answer += 'a'
    if len(answer)>15:
        answer = answer[:15].rstrip('.')
    while len(answer)<3:
        answer += answer[-1]
    return answer