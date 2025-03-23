def solution(numbers, hand):
    answer = ''
    pos = {'1':(0,0),'2':(0,1),'3':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'7':(2,0),'8':(2,1),'9':(2,2),'*':(3,0),'0':(3,1),'#':(3,2)}
    lbf = '*'
    rbf = '#'
    for n in numbers:
        n = str(n)
        if n in '147':
            answer += 'L'
            lbf = n
        elif n in '369':
            answer += 'R'
            rbf = n
        else:
            left = abs(pos[n][0]-pos[lbf][0])+abs(pos[n][1]-pos[lbf][1])
            right = abs(pos[n][0]-pos[rbf][0])+abs(pos[n][1]-pos[rbf][1])
            if left<right:
                answer += 'L'
                lbf = n
            elif left>right:
                answer += 'R'
                rbf = n
            else:
                if hand == 'right':
                    answer += 'R'
                    rbf = n
                else:
                    answer += 'L'
                    lbf = n
    return answer