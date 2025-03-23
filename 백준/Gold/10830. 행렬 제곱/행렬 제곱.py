def matMul(a,b):
  n = len(a)
  m = len(b)
  k = len(b[0])
  result = [[0]*k for _ in range(N)]
  for i in range(n):
    for j in range(k):
      for l in range(m):
        result[i][j] += a[i][l]*b[l][j] %1000
  return result

def divMatPow(a,b):
  if b==1:
    return a
  if b%2==0:
    return divMatPow(matMul(a,a),b//2)
  else:
    return matMul(divMatPow(matMul(a,a),(b-1)//2),a)

N, B = map(int,input().split())

A = []
for _ in range(N):
  A.append(list(map(int,input().split())))

result = divMatPow(A,B)
for c in result:
  for n in c:
    print(n%1000,end=" ")
  print()