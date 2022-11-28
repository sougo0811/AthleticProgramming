import sys
input = sys.stdin.readline

S = input(); Sl = list(S)
cnt = 0

for i in range(len(S)):
  if Sl[i] == "v":
    cnt+=1
  elif Sl[i] == "w":
    cnt+=2

print(cnt)