N = int(input())
G = input()
SN = []
for _ in range(N):
  s = input()
  SN.append(s)

cnt = 0
for i in range(N):
  if SN[i].find(G) != -1:
    print(SN[i])
    cnt += 1
if cnt == 0:
  print("None")