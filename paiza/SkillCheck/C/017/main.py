a,b = map(int,input().split())
n = int(input())
AN = []
BN = []
for _ in range(n):
  an,bn = map(int,input().split())
  AN.append(an)
  BN.append(bn)

for i in range(n):
  if a > AN[i]:
    print("High")
  elif a < AN[i]:
    print("Low")
  else:
    if b < BN[i]:
      print("High")
    else:
      print("Low")
