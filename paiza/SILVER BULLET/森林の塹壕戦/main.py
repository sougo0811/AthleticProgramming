N,T = map(int,input().split())
pN = []
xN = []
for _ in range(N):
  p,x = map(int,input().split())
  pN.append(p)
  xN.append(x)

exp = 0
while T != 0:
  exp += xN[T-1]
  T = pN[T-1]

print(exp,end= '\n\n')