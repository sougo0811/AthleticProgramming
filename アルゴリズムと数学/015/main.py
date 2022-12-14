A,B = map(int,input().split())

while(A >= 1 and B >= 1):
  if A > B:
    A %= B
  else:
    B %= A
if A == 0:
  print(B)
else:
  print(A)