N,M = map(int,input().split())
p_NN = []
for _ in range(N):
  p_N = list(map(int,input().split()))
  p_NN.append(p_N)

ok_routs = []
cnt = 0
for i in range(N):
  flg = True
  for j in range(N):
    if p_NN[j][i] >= M:
      flg = False
      break
  if flg == True:
    ok_routs.append(i+1)
  else:
    cnt += 1

if cnt != N:
  ok_rout = " ".join(list(map(str,ok_routs)))
  print(ok_rout)
else:
  print("wait")