#カエルの移動
def flog(N,*H):
  dp = [0]*N
  dp[1] = abs(H[0] - H[1])
  for i in range(2,N):
    dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]),dp[i-2]+abs(H[i]-H[i-2]))
  return dp

#階段の上り方
def climb_stairs(N):
  dp = [0]*(N+1)
  dp[0] = 1; dp[1] = 1
  for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp

#ナップサック問題
def knapsack(N,W,w,v):
  w,v = [0]+w,[0]+v
  dp = [[0] * (W+1) for _ in range(N+1)]

  for i in range(1,N+1):
    for j in range(W+1):
      if j < w[i]:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
  return dp

#部分和問題
def subset_sum(N,S,*A):
  dp = [[0] * (S+1) for _ in range(N)]
  dp[0][0] = 1
  #1番目のおもり
  if A[0] <= S:
    dp[0][A[0]] = 1
  #2番目以降のおもり
  for i in range(1,N):
    for j in range(S+1):
      if A[i] > j:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]
  return dp

#コイン問題

#編集距離

#重み付き区間スケジューリング問題

#巡回セールスマン問題

if __name__ == '__main__':
  #カエルの移動
  print(flog(4,10,30,40,20))
  #階段の上り方
  print(climb_stairs(6))
  #ナップサック問題
  print(knapsack(4,5,[2,1,3,2],[3,2,4,2]))
  #部分和問題
  print(subset_sum(4,15,5,1,3,4))
  #コイン問題

  #編集距離

  #重み付き区間スケジューリング問題

  #巡回セールスマン問題