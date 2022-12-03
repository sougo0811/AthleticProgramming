import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
A = []
s = 0

for i in range(N):
  a = S[i] - s
  A.append(a)
  s += a
A = " ".join(map(str, A))
print(A)