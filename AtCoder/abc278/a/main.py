import sys
input = sys.stdin.readline

N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(K):
  A.pop(0)
  A.append(0)

A =  " ".join(map(str,A))
print(A)