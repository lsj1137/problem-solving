def calScore(mid, fin, hw):
    total = mid*0.35 + fin*0.45 + hw*0.2
    return total

def calGrade(rank, total):
    step = total//10
    gradeList = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade = gradeList[rank//step]
    return grade

T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    db = {}
    scores = []
    for i in range(N):
        m,f,h = map(int, input().split())
        db[i] = calScore(m, f, h)
        scores.append(db[i])
    scores.sort(reverse=True)
    rank = scores.index(db[K-1])
    result = calGrade(rank, N)
    print(f'#{test_case} {result}')