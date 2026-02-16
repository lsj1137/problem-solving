word = input()
N = len(word)
result = 'z' * N

for i in range(1,N-1):
    for j in range(i+1, N):
        p1 = word[:i]
        p2 = word[i:j]
        p3 = word[j:]
        new_word = p1[::-1] + p2[::-1] + p3[::-1]
        if new_word<result:
            result = new_word
print(result)