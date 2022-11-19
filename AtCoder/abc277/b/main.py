import sys
input = sys.stdin.readline

N = int(input())
S = []

ans_f = ["H","D","C","S"]
ans_s = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

flg = False

for _ in range(N):
  s = input()
  S.append(s)

S_set = set(S)
if len(S_set) == N:
  for i in range(N):
    s = list(S[i])
    if s[0] in ans_f and s[1] in ans_s:
      flg = True
    else:
      flg = False
      break

if flg:
  print("Yes")
else:
  print("No")
