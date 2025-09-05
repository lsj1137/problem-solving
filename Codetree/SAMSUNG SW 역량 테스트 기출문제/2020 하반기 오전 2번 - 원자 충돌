dxy = [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

class Atom:
    def __init__(self, x, y, m, v, d):
        self.m, self.d, self.v, self.x, self.y = m, d, v, x-1, y-1

    def __str__(self):
        return f'E:{self.x=}, {self.y=}, {self.m=}, {self.d=}, {self.v=} //'

    def move(self):
        dx, dy = dxy[self.d]
        self.x = (self.x + self.v * dx + n*self.v) % n
        self.y = (self.y + self.v * dy + n*self.v) % n
        return

    def mix(self, atArr):
        for at in atArr:
            self.m += at.m
            self.v += at.v
        return 
    
    def div(self, l, newD):
        newM = self.m // 5
        newV = self.v // l
        generated = []
        if newM>0:
            for i in range(4):
                generated.append(Atom(self.x+1, self.y+1, newM, newV, 2*i+newD))
        return generated

def setNewD(atArr):
    dArr = set([])
    for at in atArr:
        dArr.add(at.d%2)
    if len(dArr)==1:
        return 0
    else:
        return 1

def moveAtoms():
    for at in atoms:
        at.move()
    return

def mixAndDivide():
    global atoms
    newAtoms = []
    for i in range(n):
        for j in range(n):
            atomInSameBlock = board[i][j]
            if len(atomInSameBlock)>1:
                rest = atomInSameBlock[1:]
                atomInSameBlock[0].mix(rest)
                generated = atomInSameBlock[0].div(len(atomInSameBlock), setNewD(atomInSameBlock))
                for newAtom in generated:
                    newAtoms.append(newAtom)
            elif len(atomInSameBlock)==1:
                newAtoms.append(atomInSameBlock[0])
    atoms = newAtoms
    return

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
atoms = [Atom(*map(int,input().split())) for _ in range(m)]

for t in range(k):
    # print(*atoms)
    moveAtoms()
    # print(*atoms)
    board = [[[] for _ in range(n)] for _ in range(n)]
    for at in atoms:
        board[at.x][at.y].append(at)
    mixAndDivide()

answer = 0
for at in atoms:
    answer += at.m
print(answer)
