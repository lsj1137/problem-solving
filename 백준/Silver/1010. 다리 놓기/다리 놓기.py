import sys

def factorial(n):
  s = 1
  for i in range(1,n+1):
    s *= i
  return s

for _ in range(int(sys.stdin.readline())):
  result = 0
  N,M = map(int,sys.stdin.readline().split())
  print(factorial(M)//(factorial(M-N)*factorial(N)))

