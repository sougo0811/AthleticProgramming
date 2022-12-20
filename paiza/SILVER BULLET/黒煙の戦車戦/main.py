H,W,K = map(int,input().split())
sH = []

for _ in range(H):
  s = list(input())
  sH.append(s)

#sH = [list(map(int,input().split())) for _ in range(H)]

ssH = sH[0]
k = ssH.index(str(K))


for i in range(1,H-1):
  if 0 == k:#左端
    while k != W-1 and sH[i][k+1] == ".":
      k+=1
  elif W-1 == k:#右端
    while k != 0 and sH[i][k-1] == ".":
      k-=1
  else:
    flg = True
    while k != 0 and sH[i][k-1] == ".":
      k-=1
      flg = False
    while flg and k != W-1 and sH[i][k+1] == ".":
      k+=1

ans = sH[H-1][k]
print(int(ans),end='\n\n')