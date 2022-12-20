import copy


H,W,N = map(int,input().split())
sH = []
for _ in range(H):
  s = list(input())
  sH.append(s)
operation = input()
op = list(operation)

ans = copy.deepcopy(sH)

#収縮
def Erosion():
  for i in range(H):
    for j in range(W):
      if sH[i][j] == ".":
        up = i-1
        down = i+1
        right = j+1
        left = j-1
        if 0<= up <= H-1:
          ans[i-1][j] = "."
        if 0<= down <= H-1:
          ans[i+1][j] = "."
        if 0<= right <= W-1:
          ans[i][j+1] = "."
        if 0<= left <= W-1:
          ans[i][j-1] = "."
  return ans

#膨張
def Dilation():
  for i in range(H):
    for j in range(W):
      if sH[i][j] == "#":
        up = i-1
        down = i+1
        right = j+1
        left = j-1
        if 0<= up <= H-1:
          ans[i-1][j] = "#"
        if 0<= down <= H-1:
          ans[i+1][j] = "#"
        if 0<= right <= W-1:
          ans[i][j+1] = "#"
        if 0<= left <= W-1:
          ans[i][j-1] = "#"
  return ans

for o in range(N):
  if op[o] == "E":
    Erosion()
    sH = copy.deepcopy(ans)
  elif op[o] == "D":
    Dilation()
    sH = copy.deepcopy(ans)

for i in range(H):
  W = "".join(sH[i])
  print(W)
