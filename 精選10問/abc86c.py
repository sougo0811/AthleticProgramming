import sys
input = sys.stdin.readline
N = int(input())
tN,xN,yN = [0],[0],[0]
for _ in range(N):
  t,x,y = map(int,input().split())
  tN.append(t); xN.append(x); yN.append(y)

for i in range(N):
  dt = tN[i+1]-tN[i]; dist = abs(xN[i+1]-xN[i])+abs(yN[i+1]-yN[i])
  if dist > dt or dt%2 != dist%2:
    print("No")
    break
else:
  print("Yes")