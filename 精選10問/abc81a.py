import sys
input = sys.stdin.readline
s = list(input())
cnt = 0
for i in range(3):
  if s[i] == "1":
    cnt+=1
print(cnt)