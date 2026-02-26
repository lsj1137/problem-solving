N = int(input())
S = input()
vowel = set(['a', 'e', 'i', 'o', 'u'])
answer = 0
for c in S:
    if c in vowel:
        answer += 1
print(answer)