N = int(input())
AN = []
BN = []
for _ in range(N):
  a,b = map(int,input().split())
  AN.append(a)
  BN.append(b)

for i in range(N):
  flg = False
  a = list(str(AN[i]))
  b = (BN[i])
  if b == int(a[0])+int(a[1])+int(a[2]):
    flg = True
  if b == int(a[0])*10+int(a[1])+int(a[2]):
    flg = True
  if b == int(a[0])*10+int(a[2])+int(a[1]):
    flg = True
  if int(a[1]) != 0:
    if b == int(a[1])*10+int(a[0])+int(a[2]):
      flg = True
    if b == int(a[1])*10+int(a[2])+int(a[0]):
      flg = True
  if int(a[2]) != 0:
    if b == int(a[2])*10+int(a[0])+int(a[1]):
      flg = True
    if b == int(a[2])*10+int(a[1])+int(a[2]):
      flg = True
  if flg:
    print("Yes")
  else:
    print("No")