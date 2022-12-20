S = input()
S = list(S)
N = int(input())
xN = []
yN = []
for _ in range(N):
  x,y = map(int,input().split())
  xN.append(x)
  yN.append(y)

for i in range(N):
  for j in range(xN[i],yN[i]+1):
    if S[j] == "0":
      S[j] = 1
    else:
      S[j] = 0

S = "".join(S)
print(S)