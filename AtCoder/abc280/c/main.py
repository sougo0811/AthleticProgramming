import sys
input = sys.stdin.readline

S = list(input())
T = list(input())

cnt = 1

for i in range(len(S)):
  if S[i] == T[i]:
    cnt += 1
  else:
    print(cnt)
    break
