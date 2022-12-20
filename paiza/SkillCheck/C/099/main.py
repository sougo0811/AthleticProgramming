N,D = map(int,input().split())
DN = []
for _ in range(1,N):
  d = int(input())
  DN.append(d)

X = D
for i in range(len(DN)):
  X += D-DN[i]
print(D*X)