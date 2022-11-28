import sys
input = sys.stdin.readline

X,Y,Z = map(int,input().split())

if (X < 0 and Y > 0) or (X > 0 and Y < 0) or (abs(Y)-abs(X) > 0):
  print(abs(X))
else:
  if Y > 0 and Z < Y:
    if Z < 0:
      print(-2*Z+X)
    else:
      print(abs(X))
  elif Y < 0 and Z > Y :
    if Z > 0:
      print(2*Z+abs(X))
    else:
      print(abs(X))
  else:
    print(-1)