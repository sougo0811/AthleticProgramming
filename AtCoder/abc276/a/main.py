S = input()
S = list(S)
S = list(reversed(S))

if "a" in S:
  ans = len(S) - S.index("a")
  print(ans)
else:
  print(-1)