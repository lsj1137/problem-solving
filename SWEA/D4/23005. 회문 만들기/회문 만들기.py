for _ in range(int(input())):
  S = input()
  start = 0
  end = len(S)-1
  answer = 0
  while start<end:
    if S[start]!=S[end]:
      if S[start] == 'x' :
        answer += 1
        start += 1
      elif S[end] == 'x':
        answer += 1
        end -= 1
      else :
        answer = -1
        break
    else:
      start+=1
      end-=1
  print(answer)
