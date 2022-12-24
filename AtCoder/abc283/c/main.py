import sys
input = sys.stdin.readline

S = input()
cnt = 0
zeroflg = False
for i in range(len(S)-1):
  if S[i] == '0':
    if  zeroflg:
      cnt += 1
      zeroflg = False
    else:
      zeroflg = True
  else:
    if zeroflg:
      cnt+=1
      zeroflg = False
    cnt += 1
if zeroflg:
  cnt += 1
print(cnt)