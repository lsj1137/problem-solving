def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tempRow = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            tempRow.append(temp)
        answer.append(tempRow)
    return answer