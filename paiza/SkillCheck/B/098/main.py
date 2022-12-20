N,M,T,K = map(int,input().split())
a = [list(map(int, input().split())) for l in range(M)]

for j in range(N):
  flg = False
  hour = 0
  point = 0
  for i in range(M):
    point += a[i][j]
    hour += 1
    if hour > T:
      point -= a[i-T][j]
    if point >= K:
      flg = True
      break
  if flg == True:
    print("yes"+" "+str(i+1))
  else:
    print("no"+" "+str(0))
