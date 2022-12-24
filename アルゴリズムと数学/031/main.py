N = int(input())
A = list(map(int,input().split()))

dp_y = [0]*(N+1); dp_n = [0]*(N+1)
for i in range(1,N+1):
  dp_y[i] = dp_n[i-1] + A[i-1]
  dp_n[i] = max(dp_y[i-1],dp_n[i-1])

print(max(dp_y[N],dp_n[N]))