import sys
input = sys.stdin.readline
N = int(input())
dN = []
for _ in range(N):
  dN.append(int(input()))
dN.sort();dN = set(dN)
print(len(dN))