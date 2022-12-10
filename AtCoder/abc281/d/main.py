import sys
input = sys.stdin.readline

import itertools

N,K,D = map(int,input().split())
A = list(map(int,input().split()))

#TEL
Sa = list(itertools.combinations(A,K))
Sb = [sum(i) for i in Sa if sum(i)%D == 0]
S = set(Sb)
if len(S) == 0:
  print(-1)
else:
  print(max(S))
