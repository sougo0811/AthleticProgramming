N,M = map(int,input().split())
fM = []
for _ in range(M):
  f = int(input())
  fM.append(f)

point = 0

for i in range(M):
  flg = True
  if flg == True and point >= fM[i]:
    point -= fM[i]
    flg = False
  elif flg == True and point < fM[i]:
    N -= fM[i]
    point += (fM[i]*0.1)
    flg = False
  print(str(N) + " " + str(int(point)))