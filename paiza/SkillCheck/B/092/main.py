import numpy as np

H,W,K = map(int,input().split())
sH = []
for _ in range(H):
  s = list(input())
  sH.append(s)
#print(sH)
N = np.array(sH)
save = np.argwhere(N=="N")
save = save.tolist()
long = 0
short = 999999
shorts = [1]
for i in range(1,K+1):
  point = np.argwhere(N==str(i))
  point = point.tolist()
  high = abs(save[0][0] - point[0][0])
  wid = abs(save[0][1] - point[0][1])
  long = high + wid
  if long < short:
    shorts.clear()
    short = long
    shorts.append(str(i))
  elif long == short:
    shorts.append(str(i))
    short = long

print(len(shorts))
for j in shorts:
  print(j)