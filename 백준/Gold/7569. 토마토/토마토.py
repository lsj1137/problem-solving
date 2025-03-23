import sys
M,N,H = map(int,sys.stdin.readline().split())
tmtmap = [[[None]*M for _ in range(N)] for _ in range(H)]
st = []
depth,result = 0,-1
for k in range(H):
  for i in range(N):
    tmtmap[k][i]=list(sys.stdin.readline().split())
    for j in range(M):
      if tmtmap[k][i][j] == '1':
        st.append([k,i,j])
finish = False
while st and not finish:
  newst = set([])
  for p in st:
    if tmtmap[p[0]][p[1]][p[2]]=='-1':
      continue
    if p[0]>0 and tmtmap[p[0]-1][p[1]][p[2]]=='0':
      newst.add((p[0]-1,p[1],p[2]))
    if p[1]>0 and tmtmap[p[0]][p[1]-1][p[2]]=='0':
      newst.add((p[0],p[1]-1,p[2]))
    if p[2]>0 and tmtmap[p[0]][p[1]][p[2]-1]=='0':
      newst.add((p[0],p[1],p[2]-1))
    if p[0]<H-1 and tmtmap[p[0]+1][p[1]][p[2]]=='0':
      newst.add((p[0]+1,p[1],p[2]))
    if p[1]<N-1 and tmtmap[p[0]][p[1]+1][p[2]]=='0':
      newst.add((p[0],p[1]+1,p[2]))
    if p[2]<M-1 and tmtmap[p[0]][p[1]][p[2]+1]=='0':
      newst.add((p[0],p[1],p[2]+1))
    tmtmap[p[0]][p[1]][p[2]] = '1'
  for i in range(H):
    for j in range(N):
      if '0' in tmtmap[i][j]:
        break
      if i==H-1 and j==N-1:
        result = depth
        finish = True
    if '0' in tmtmap[i][j]:
        break
  if len(newst) == 0 and not finish:
    result = -1
  st = list(newst)
  depth += 1
print(result)