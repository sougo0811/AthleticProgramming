import sys
input = sys.stdin.readline

H,W = map(int,input().split())
C = [[] for _ in range(H)]
for i in range(H):
  c = input()
  C[i] = list(c)


tr = []
for i in range(W):
  tr_row = []
  for vector in C:
    tr_row.append(vector[i])
  tr.append(tr_row)

ans = []

for i in range(W):
  cnt = 0
  for j in range(H):
    if tr[i][j] == '#':
      cnt+=1
  ans.append(cnt)

ans = " ".join(map(str,ans))
print(ans)