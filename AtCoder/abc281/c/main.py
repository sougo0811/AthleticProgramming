import sys
input = sys.stdin.readline

N,T = map(int,input().split())
A = list(map(int,input().split()))
Atotal = sum(A); T%=Atotal
cnt = 0
for i in range(N):
  if T - (cnt+A[i]) <= 0:
    print(str(i+1) + " " + str(T-cnt))
    break
  cnt += A[i]