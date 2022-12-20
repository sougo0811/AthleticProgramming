import copy
H,W = map(int,input().split())
SH = []
bom = 0
cnt = 0
for _ in range(H):
  s = input()
  s = list(s)
  SH.append(s)
  bom += s.count("#")

SH_C = copy.deepcopy(SH)

for j in range(H):
  if "#" in SH[j]:
    b = [n for n, v in enumerate(SH[j]) if v == "#"]
    for i in range(W):
      SH_C[j][i] = "#"
    for k in range(len(b)):
      for l in range(H):
        SH_C[l][b[k]] = "#"
for i in range(H):
  cnt += SH_C[i].count("#")
print(cnt)