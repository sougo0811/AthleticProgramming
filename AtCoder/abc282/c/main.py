import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
S = list(S)

flg = 0
for i in range(N):
  if S[i] == "\"":
    flg += 1
  if flg%2 == 0:
    if S[i] == ",":
      S[i] = "."
S = "".join(S)
print(S)
