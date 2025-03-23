def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
        if len(numbers[i])==1:
            numbers[i] = (numbers[i]*4,numbers[i])
        elif len(numbers[i])==2:
            numbers[i] = (numbers[i]*2,numbers[i])
        elif len(numbers[i])==3:
            numbers[i] = (numbers[i]+numbers[i][0],numbers[i])
        else:
            numbers[i] = (numbers[i],numbers[i])
    numbers.sort(key = lambda x: x[0],reverse = True)
    answer = str(int(''.join([x[1] for x in numbers])))
    return answer