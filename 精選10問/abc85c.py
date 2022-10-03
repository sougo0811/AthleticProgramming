import sys
input = sys.stdin.readline
N,M = map(int,input().split())
X = 0; Y = 0; Z = 0; total = 0
for x in range(N+1):
  for y in range(N+1):
    total = 10000*x + 5000*y + 1000*(N-(x+y))
    if x + y + N-(x+y) == N and total == M and N-(x+y)>=0:
      X,Y,Z = x,y,N-(x+y)
      break
if X == 0 and Y == 0 and Z == 0:
  print("-1 -1 -1")
else:
  print(str(X)+" "+str(Y)+" "+str(Z))