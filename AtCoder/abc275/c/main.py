import sys
input = sys.stdin.readline
'''
S = []
for _ in range(9):
  s = list(input())
  S.append(s)

ans = 0
for i in range(9):
  for j in range(9):
    if i <= j: 
      a = 9-j
    else:
      a = 9-i
    for k in range(1,a+1):
      for l in range(1,a+1):
        if S[i][j] == "#":
          if S[i][j+k] == "#" and S[i+k][j] == "#" and S[i+k][j+k] == "#":
            ans += 1
          if S[i+k][j+k] == "#" and S[i-k][j+k] == "#" and S[i][j+k*2] == "#":
            ans += 1
          if S[i+k][j+l] == "#" and S[i-l][j+k] == "#" and S[i-k][j+k+l] == "#":
            ans += 1
'''

import itertools
S=[input() for _ in range(9)]
#print(S)
ans=0
for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
  #print(i1,j1,i2,j2)
  # (i1,j1)から→↓の向きに(i2,j2)がある
  if i2>i1 and j2>=j1 and S[i1][j1]=="#" and S[i2][j2]=="#":
    di=i2-i1
    dj=j2-j1
    i3=i2+dj
    j3=j2-di
    i4=i3-di
    j4=j3-dj
    if 0<=i3<9 and 0<=j3<9 and 0<=i4<9 and 0<=j4<9 and S[i3][j3]=="#" and S[i4][j4]=="#":
      ans+=1
print(ans)