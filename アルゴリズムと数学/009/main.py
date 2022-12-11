import sys
input = sys.stdin.readline
N,S = map(int,input().split())
A = list(map(int,input().split()))

#愚直
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

#動的計画法(DP)
