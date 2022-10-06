import sys
input = sys.stdin.readline
N = int(input())
ans = 0

def divisor(n):
  cnt = 0
  for i in range(1,n+1):
    if n%i == 0:
      cnt += 1
  return cnt

for n in range(1,N+1,2):
  cnt = divisor(n)
  if cnt == 8:
    ans += 1
print(ans)