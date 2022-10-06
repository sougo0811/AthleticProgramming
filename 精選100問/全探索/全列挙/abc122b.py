import sys
input = sys.stdin.readline
S = input()
agct = ["A","C","G","T"]
cnt = 0; ans = 0
for i in range(len(S)):
  if S[i] in agct:
    cnt += 1
  else:
    cnt = 0
  ans = max(ans,cnt)
print(ans)