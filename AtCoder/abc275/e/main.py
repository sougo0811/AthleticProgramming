import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

max_N = N+1
dp = [[0]*(N+1) for _ in range(K)]

for i in range(K):
  dp[i][0] = 1

for j in range(N+1):
  dp[0][j] = 1


print(dp[K][M])