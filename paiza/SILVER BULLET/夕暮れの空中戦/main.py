import string

N = int(input())
SN = []

block = []
for _ in range(N+2):
  block.append("#")

SN.append(block)
for _ in range(N):
  b = "#"
  s = (input())
  s = list(s)
  s.insert(0,"#")
  s.append("#")
  SN.append(s)
SN.append(block)

alf = list(string.ascii_letters)
cnt = 0
ans = "No"
for i in range(1,N+1):
  for j in range(1,N+1):
    if SN[i][j] == "." and SN[i+1][j] == "." and SN[i+1][j+1] == ".":
      SN[i][j] = alf[cnt]
      SN[i+1][j] = alf[cnt]
      SN[i+1][j+1] = alf[cnt]
      ans = "Yes"
      cnt += 1
    elif SN[i+1][j] == "." and SN[i+1][j+1] == "." and SN[i][j+1] == ".":
      SN[i+1][j] = alf[cnt]
      SN[i+1][j+1] = alf[cnt]
      SN[i][j+1] = alf[cnt]
      ans = "Yes"
      cnt += 1
    elif SN[i][j] == "." and SN[i][j+1] == "." and SN[i+1][j+1] == ".":
      SN[i][j] = alf[cnt]
      SN[i][j+1] = alf[cnt]
      SN[i+1][j+1] = alf[cnt]
      ans = "Yes"
      cnt += 1
    elif SN[i][j] == "." and SN[i][j+1] == "." and SN[i+1][j] == ".":
      SN[i][j] = alf[cnt]
      SN[i][j+1] = alf[cnt]
      SN[i+1][j] = alf[cnt]
      ans = "Yes"
      cnt += 1

if ans == "Yes":
  print(ans)
  for i in range(1,N+1):
    ans_l = SN[i]
    ans_l = ans_l[1:-1]
    ans_l = "".join(ans_l)
    print(ans_l)
else:
  print(ans)
