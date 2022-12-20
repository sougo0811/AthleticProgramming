N = int(input())
hNN = []
over = [int(0) for i in range(N+2)]
hNN.append(over)
for _ in range(N):
  hN = list(map(int,input().split()))
  hN.insert(0,0)
  hN.append(0)
  hNN.append(hN)
hNN.append(over)

top = []
for i in range(1,N+1):
  for j in range(1,N+1):
    if hNN[i][j] > hNN[i+1][j] and hNN[i][j] > hNN[i-1][j] and hNN[i][j] > hNN[i][j+1] and hNN[i][j] > hNN[i][j-1]:
      top.append(hNN[i][j])

top = sorted(top, reverse=True)
for t in top:
  print(t)