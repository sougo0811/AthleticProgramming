E = input()
E = list(E)

ans = 0
cnt = 0
for i in range(len(E)):
  if E[i] == "/":
    cnt += 1
  elif E[i] == "<":
    cnt += 10
  else:
    ans += cnt
    cnt = 0

print(ans+cnt)