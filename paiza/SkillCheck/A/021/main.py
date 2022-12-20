import copy
H,W = map(int,input().split())
sea = ["." for _ in range(W+2)]
SH = []
for _ in range(H):
  S = list(input())
  S.insert(0,".")
  S.append(".")
  SH.append(S)
SH.insert(0,sea)
SH.append(sea)
#print(SH)

for i in range(H+2):
  print(SH[i])

'''
island = []
coast = []
undiscovered_tmp = []
undiscovered = []
discovered = []
for i in range(1,H+1):
  for j in range(1,W+1):
    if SH[i][j] == "#":
      y = i
      x = j
      undiscovered.append([y,x])
print(undiscovered)

undiscovered_tmp = copy.deepcopy(undiscovered)


for i in range(len(undiscovered_tmp)):
  flg = True
  a = undiscovered_tmp[i]
  if [a[0],a[1]+1] in undiscovered:
    discovered.append([a[0],a[1]+1])
    flg = False
  if [a[0],a[1]-1] in undiscovered:
    discovered.append([a[0],a[1]-1])
    flg = False
  if [a[0]+1,a[1]] in undiscovered:
    discovered.append([a[0]+1,a[1]])
    flg = False
  if [a[0]-1,a[1]] in undiscovered:
    discovered.append([a[0]-1,a[1]])
    flg = False
  if flg:
    undiscovered.pop(i)
    continue
  else:
    while len(discovered) != 0:
      
'''