import sys
input = sys.stdin.readline

H,W = map(int,input().split())

S = [[0] * H for _ in range(W)]
T = [[0] * H for _ in range(W)]
#S
for i in range(H):
  a = list(input())
  for j in range(W):
    S[j][i] = a[j]
#T
for i in range(H):
  a = list(input())
  for j in range(W):
    T[j][i] = a[j]

S_ans = [];T_ans = []
for i in range(W):
  S_ans.append("".join(S[i]))
  T_ans.append("".join(T[i]))
S_ans = sorted(S_ans)
T_ans = sorted(T_ans)

if S_ans == T_ans:
  print("Yes")
else:
  print("No")