import sys
input = sys.stdin.readline
N,S = map(int,input().split())
A = list(map(int,input().split()))

#愚直
'''
import itertools
flg = 0
for i in range(1,N+1):
  Sa = list(itertools.combinations(A,i))
  Sb = [sum(i) for i in Sa]
  Sc = set(Sb)
  if S in Sc:
    flg = 1
    break
if flg:
  print("Yes")
else:
  print("No")
'''
#動的計画法(DP)
dp = [[0] * (S+1) for _ in range(N)]
dp[0][0] = 1
if A[0] <= S:
  dp[0][A[0]] = 1
for i in range(1,N):
  for j in range(S+1):
    if A[i] > j:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]
print("Yes" if dp[-1][-1] else "No")