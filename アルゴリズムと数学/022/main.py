N = int(input())
A = list(map(int,input().split()))
memo = [0]*100000; cnt = 0

for i in range(N):
  memo[A[i]] += 1

for i in range(1,50001):
  if i == 50000:
    cnt += memo[i]*(memo[i]-1)//2
  else:
    cnt += memo[i]*memo[100000-i]

print(cnt)