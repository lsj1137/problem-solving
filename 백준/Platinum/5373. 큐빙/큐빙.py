top = [['w','w','w'],['w','w','w'],['w','w','w']]
front = [['r','r','r'],['r','r','r'],['r','r','r']]
right = [['b','b','b'],['b','b','b'],['b','b','b']]
back = [['o','o','o'],['o','o','o'],['o','o','o']]
left = [['g','g','g'],['g','g','g'],['g','g','g']]
bottom = [['y','y','y'],['y','y','y'],['y','y','y']]

def rotateOneFace(face, direction):
    temp1 = [face[0][0], face[0][1], face[0][2]] #위
    temp2 = [face[0][2], face[1][2], face[2][2]] #오른쪽
    temp3 = [face[2][2], face[2][1], face[2][0]] #아래
    temp4 = [face[2][0], face[1][0], face[0][0]] #왼쪽
    if direction=='+':
        face[0][2], face[1][2], face[2][2] = temp1 #오른쪽에 위에거
        face[2][2], face[2][1], face[2][0] = temp2 #아래쪽에 오른쪽거
        face[2][0], face[1][0], face[0][0] = temp3 #왼쪽에 아래쪽거
        face[0][0], face[0][1], face[0][2] = temp4 #위쪽에 왼쪽거
    else:
        face[0][2], face[1][2], face[2][2] = temp3 #오른쪽에 아래쪽거
        face[2][2], face[2][1], face[2][0] = temp4 #아래쪽에 왼쪽거
        face[2][0], face[1][0], face[0][0] = temp1 #왼쪽에 위쪽거
        face[0][0], face[0][1], face[0][2] = temp2 #위쪽에 오른쪽거
    
def rotateFourEdges(face, direction):
    if face=='U':
        temp1 = [back[0][0], back[0][1], back[0][2]] #뒤
        temp2 = [right[0][0], right[0][1], right[0][2]] #오른쪽
        temp3 = [front[0][0], front[0][1], front[0][2]] #앞
        temp4 = [left[0][0], left[0][1], left[0][2]] #왼쪽
        if direction=='+':
            right[0][0], right[0][1], right[0][2] = temp1
            front[0][0], front[0][1], front[0][2] = temp2
            left[0][0], left[0][1], left[0][2] = temp3
            back[0][0], back[0][1], back[0][2] = temp4
        else:
            right[0][0], right[0][1], right[0][2] = temp3
            front[0][0], front[0][1], front[0][2] = temp4
            left[0][0], left[0][1], left[0][2] = temp1
            back[0][0], back[0][1], back[0][2] = temp2
    elif face=='F':
        temp1 = [top[2][0], top[2][1], top[2][2]] #위
        temp2 = [right[0][0], right[1][0], right[2][0]] #오른쪽
        temp3 = [bottom[0][2], bottom[0][1], bottom[0][0]] #밑
        temp4 = [left[2][2], left[1][2], left[0][2]] #왼쪽
        if direction=='+':
            right[0][0], right[1][0], right[2][0] = temp1
            bottom[0][2], bottom[0][1], bottom[0][0] = temp2
            left[2][2], left[1][2], left[0][2] = temp3
            top[2][0], top[2][1], top[2][2] = temp4
        else:
            right[0][0], right[1][0], right[2][0] = temp3
            bottom[0][2], bottom[0][1], bottom[0][0] = temp4
            left[2][2], left[1][2], left[0][2] = temp1
            top[2][0], top[2][1], top[2][2] = temp2
    elif face=='R':
        temp1 = [top[2][2], top[1][2], top[0][2]] #위
        temp2 = [back[0][0], back[1][0], back[2][0]] #뒤
        temp3 = [bottom[2][2], bottom[1][2], bottom[0][2]] #밑
        temp4 = [front[2][2], front[1][2], front[0][2]] #앞
        if direction=='+':
            back[0][0], back[1][0], back[2][0] = temp1
            bottom[2][2], bottom[1][2], bottom[0][2] = temp2
            front[2][2], front[1][2], front[0][2] = temp3
            top[2][2], top[1][2], top[0][2] = temp4
        else:
            back[0][0], back[1][0], back[2][0] = temp3
            bottom[2][2], bottom[1][2], bottom[0][2] = temp4
            front[2][2], front[1][2], front[0][2] = temp1
            top[2][2], top[1][2], top[0][2] = temp2
    elif face=='B':
        temp1 = [top[0][2], top[0][1], top[0][0]] #위
        temp2 = [left[0][0], left[1][0], left[2][0]] #왼쪽
        temp3 = [bottom[2][0], bottom[2][1], bottom[2][2]] #밑
        temp4 = [right[2][2], right[1][2], right[0][2]] #오른쪽
        if direction=='+':
            left[0][0], left[1][0], left[2][0] = temp1
            bottom[2][0], bottom[2][1], bottom[2][2] = temp2
            right[2][2], right[1][2], right[0][2] = temp3
            top[0][2], top[0][1], top[0][0] = temp4
        else:
            left[0][0], left[1][0], left[2][0] = temp3
            bottom[2][0], bottom[2][1], bottom[2][2] = temp4
            right[2][2], right[1][2], right[0][2] = temp1
            top[0][2], top[0][1], top[0][0] = temp2
    elif face=='L':
        temp1 = [top[0][0], top[1][0], top[2][0]] #위
        temp2 = [front[0][0], front[1][0], front[2][0]] #앞
        temp3 = [bottom[0][0], bottom[1][0], bottom[2][0]] #밑
        temp4 = [back[2][2], back[1][2], back[0][2]] #뒤
        if direction=='+':
            front[0][0], front[1][0], front[2][0] = temp1
            bottom[0][0], bottom[1][0], bottom[2][0] = temp2
            back[2][2], back[1][2], back[0][2] = temp3
            top[0][0], top[1][0], top[2][0] = temp4
        else:
            front[0][0], front[1][0], front[2][0] = temp3
            bottom[0][0], bottom[1][0], bottom[2][0] = temp4
            back[2][2], back[1][2], back[0][2] = temp1
            top[0][0], top[1][0], top[2][0] = temp2
    elif face=='D':
        temp1 = [front[2][0], front[2][1], front[2][2]] #앞
        temp2 = [right[2][0], right[2][1], right[2][2]] #오른쪽
        temp3 = [back[2][0], back[2][1], back[2][2]] #뒤
        temp4 = [left[2][0], left[2][1], left[2][2]] #왼쪽
        if direction=='+':
            right[2][0], right[2][1], right[2][2] = temp1
            back[2][0], back[2][1], back[2][2] = temp2
            left[2][0], left[2][1], left[2][2] = temp3
            front[2][0], front[2][1], front[2][2] = temp4
        else:
            right[2][0], right[2][1], right[2][2] = temp3
            back[2][0], back[2][1], back[2][2] = temp4
            left[2][0], left[2][1], left[2][2] = temp1
            front[2][0], front[2][1], front[2][2] = temp2

def rotate(face, direction):
    if face=='U':
        rotateOneFace(top, direction)
    elif face=='F':
        rotateOneFace(front, direction)
    elif face=='R':
        rotateOneFace(right, direction)
    elif face=='B':
        rotateOneFace(back, direction)
    elif face=='L':
        rotateOneFace(left, direction)
    elif face=='D':
        rotateOneFace(bottom, direction)
    rotateFourEdges(face, direction)



for _ in range(int(input())):
    rotateCount = int(input())
    rotateList = input().split()
    for i in range(rotateCount):
        face = rotateList[i][0]
        direction = rotateList[i][1]
        rotate(face,direction)
    for f in top:
        print(''.join(f))
    top = [['w','w','w'],['w','w','w'],['w','w','w']]
    front = [['r','r','r'],['r','r','r'],['r','r','r']]
    right = [['b','b','b'],['b','b','b'],['b','b','b']]
    back = [['o','o','o'],['o','o','o'],['o','o','o']]
    left = [['g','g','g'],['g','g','g'],['g','g','g']]
    bottom = [['y','y','y'],['y','y','y'],['y','y','y']]