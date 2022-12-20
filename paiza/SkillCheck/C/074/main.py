H,W,X = map(int,input().split())
S = ""
for _ in range(H):
  s = input()
  S+=s

S = list(S)
cnt = 0
ans = ""

for i in range(len(S)):
  if cnt%X == 0 and cnt != 0:
    print(ans)
    ans = ""
  ans += S[i]
  cnt += 1
print(ans)
