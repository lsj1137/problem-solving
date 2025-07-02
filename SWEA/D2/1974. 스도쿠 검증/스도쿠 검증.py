def check(arr):
    checked = [True]+ [False for _ in range(9)]
    for i in arr:
        checked[i]=True
    if False in checked:
        return False
    else:
        return True

T = int(input())
for test_case in range(1, T + 1):
    sudoku = []
    answer = 1
    for _ in range(9):
        line = list(map(int,input().split()))
        if not check(line):
            answer = 0
        sudoku.append(line)
    for i in range(9):
        arr1 = []
        arr2 = []
        for j in range(9):
            arr1.append(sudoku[j][i])
            arr2.append(sudoku[i//3*3+j//3][i%3*3+j%3])
        if not check(arr1):
            answer = 0
        if not check(arr2):
            answer = 0

    print(f'#{test_case} {answer}')