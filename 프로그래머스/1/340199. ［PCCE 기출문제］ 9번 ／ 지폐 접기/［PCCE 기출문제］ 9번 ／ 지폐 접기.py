def solution(wallet, bill):
    answer = 0
    wallet.sort()
    newBill = sorted(bill[:])
    while newBill[0]>wallet[0] or newBill[1]>wallet[1]:
        newBill[1] //= 2
        newBill.sort()
        answer += 1
    return answer