N,x_1 = map(int,input().split())
dN = list(map(int,input().split()))
xN = [x_1]
for i in range(N-1):
  if i == 0:
    xN.append(dN[i] - xN[i])
  else:
    xN.append(dN[i] - xN[i-1] - xN[i])
ans = " ".join(map(str, xN))
print(ans)