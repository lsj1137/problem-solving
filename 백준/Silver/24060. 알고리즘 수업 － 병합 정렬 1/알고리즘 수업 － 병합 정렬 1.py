def merge_sort(arr, s_i, e_i):
    if (s_i<e_i):
        mid = (s_i + e_i) // 2
        merge_sort(arr, s_i, mid)
        merge_sort(arr, mid+1, e_i)
        merge(arr, s_i, mid, e_i)

def merge(arr, s_i, mid, e_i):
    global save_count, answer
    i = s_i
    j = mid+1
    tmp = []
    while i<=mid and j<=e_i:
        if (arr[i]<=arr[j]):
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=mid:
        tmp.append(arr[i])
        i+=1
    while j<=e_i:
        tmp.append(arr[j])
        j+=1
    i = s_i
    t = 0
    while i<=e_i:
        arr[i] = tmp[t]
        save_count += 1
        if save_count==K:
            answer = arr[i]
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
save_count = 0
answer = -1

merge_sort(A, 0, len(A)-1)
print(answer)