import sys
input = sys.stdin.readline
from collections import defaultdict

N,Q = map(int,input().split())
T,A,B = [],[],[]
for _ in range(Q):
  t,a,b = map(int,input().split())
  T.append(t); A.append(a); B.append(b)

users = [[0] * (N+1) for _ in range(N+1)]
#users = defaultdict()

for i in range(Q):
  if T[i] == 1:
    if 0 == users[A[i]][B[i]]:
      users[A[i]][B[i]] = 1
  elif T[i] == 2:
    if 1 == users[A[i]][B[i]]:
      users[A[i]][B[i]] = 0
  elif T[i] == 3:
    if 1 == users[A[i]][B[i]] and 1 == users[B[i]][A[i]]:
      print("Yes")
    else:
      print("No")
