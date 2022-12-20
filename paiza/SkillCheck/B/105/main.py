N,H,W = map(int,input().split())
AN = []; BN = []; CN = []
for i in range(3*N):
  if i%3 == 0:
    AN.append(list(map(int,input().split())))
  elif i%3 == 1:
    BN.append(list(map(int,input().split())))
  else:
    CN.append(list(map(int,input().split())))

for j in range(N):
  if AN[j][0]+AN[j][2] > W:
    print(0)