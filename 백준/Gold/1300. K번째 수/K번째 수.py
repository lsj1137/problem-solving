def find_index(size, n):
    result = 0
    for i in range(1, min(size+1, n)):
        result += min(size*i, n-1)//i
    return result

def count_same(size, n):
    result = 0
    for i in range(1, min(size+1, n+1)):
        if n%i==0 and n//i<=size:
            result += 1
    return result

def search_kth_num(s, e, k, size):
    while s<e:
        mid = (s+e)//2
        ind = find_index(size, mid)+1
        count = count_same(size, mid)
        # print("mid, ind, count >> :", mid, ind, count)
        if count!=0 and ind<=k and k<ind+count:
            return mid
        if ind <= k:
            s = mid+1
        else:
            e = mid
    return mid

N = int(input())
K = int(input())
answer = search_kth_num(1, N**2+1, K, N)
print(answer)
