def toBinary(num):
  result = ''
  while num>0:
    result += str(num%2)
    num //= 2
  return result[::-1].zfill(6)

def toAlpha(binary):
  result = 0
  for i in range(len(binary)):
    result += int(binary[i]) * 2**(len(binary)-1-i)
  return chr(result)
  
dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, 'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37, 'm':38, 'n':39, 'o':40, 'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, 'w':48, 'x':49, 'y':50, 'z':51, '0':52, '1':53, '2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, '9':61, '+':62, '/':63}

T = int(input())
for test_case in range(1, T + 1):
  code = input()
  s = ''
  result = ''
  for c in code:
    s+= toBinary(dict[c])
  for i in range(0, len(s), 8):
    binS = s[i:i+8]
    result += toAlpha(binS)
  print(f'#{test_case} {result}')
