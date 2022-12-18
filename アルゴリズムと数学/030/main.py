N,W = map(int,input().split())
w,v = [0],[0]
for i in range(N):
  a,b = map(int,input().split())
  w.append(a); v.append(b)

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(W+1):
    if j < w[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])

print(dp[N][W])