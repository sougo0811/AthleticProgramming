N = int(input())
SN = []
for _ in range(N):
  s = int(input())
  SN.append(s)
M = int(input())
abxm = []
for _ in range(M):
  abx = list(map(int,input().split()))
  abxm.append(abx)

for i in range(M):
  if abxm[i][2] <= SN[abxm[i][0]-1]:
    SN[abxm[i][1]-1]+= abxm[i][2]
    SN[abxm[i][0]-1]-= abxm[i][2]
  else:
    SN[abxm[i][1]-1]+= SN[abxm[i][0]-1]
    SN[abxm[i][0]-1] = 0

for j in range(N):
  print(SN[j])