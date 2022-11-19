import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

query = []
for _ in range(Q):
  q = list(map(int,input().split()))
  query.append(q)

for i in range(Q):
  q = query[i]
  if q[0] == 1:
    A = [q[1]] * len(A)
  elif q[0] == 2:
    A[q[1]-1] += q[2]
  elif q[0] == 3:
    print(A[q[1]-1])