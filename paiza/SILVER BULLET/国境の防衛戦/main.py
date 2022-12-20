N = int(input())
SN = []
for _ in range(N):
  s = input()
  SN.append(s)

for i in range(N):
  s = list(SN[i])
  for j in range(len(s)):
    if s[j] == "/":
      if s[j+1] == "/":
        s[j:] = ""
        break
  s = "".join(s)
  print(s)